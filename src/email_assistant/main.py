"""Application entry point."""
from email_assistant.config import settings
from email_assistant.gmail import connect_imap, connect_smtp
from email_assistant.gmail.client import compose_text_email, fetch_new_message, send_message
from email_assistant.llm.OpenRouter import generate_response

import email
from email.utils import parseaddr

def main():
    imap = connect_imap(settings)
    smtp = connect_smtp(settings)

    _, msg_data = fetch_new_message(imap)

    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    email_subject = msg["Subject"]
    email_from = msg["From"]
    email_body = ""

    if msg.is_multipart():
        for part in msg.get_payload():
            if part.get_content_type() == "text/plain":
                email_body = part.get_payload(decode=True).decode(errors="ignore")
                break
    else:
        email_body = msg.get_payload(decode=True).decode(errors="ignore")


    
    response = generate_response(email_subject, email_body, email_from).strip()
    print(response)

    recipient = parseaddr(email_from)[1]
    reply_subject = (
        email_subject if (email_subject or "").lower().startswith("re:") else f"Re: {email_subject or ''}"
    )
    parent_message_id = msg.get("Message-Id")
    references = msg.get("References")
    if parent_message_id and references:
        references = f"{references} {parent_message_id}".strip()
    elif parent_message_id:
        references = parent_message_id

    reply_bytes = compose_text_email(
        from_addr=settings.email,
        to_addrs=[recipient],
        subject=reply_subject,
        body=response,
        in_reply_to=parent_message_id,
        references=references,
    )
    send_message(
        smtp=smtp,
        from_addr=settings.email,
        to_addrs=[recipient],
        message_bytes=reply_bytes,
    )

    imap.logout()
    smtp.quit()
    


if __name__ == "__main__":
    main()
