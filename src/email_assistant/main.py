"""Application entry point."""
from email_assistant.config import settings
from email_assistant.gmail import connect_imap, connect_smtp
from email_assistant.gmail.client import compose_text_email, fetch_new_message, send_message
from email_assistant.llm.OpenRouter import generate_response
from email_assistant.agent.filter import emailValidatorLLM


import email
from email.utils import parseaddr

def main():
    imap = connect_imap(settings)
    smtp = connect_smtp(settings)

    _, msg_data = fetch_new_message(imap)

    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    emailSubject = msg["Subject"]
    emailFrom = msg["From"]
    emailBody = ""

    if msg.is_multipart():
        for part in msg.get_payload():
            if part.get_content_type() == "text/plain":
                emailBody = part.get_payload(decode=True).decode(errors="ignore")
                break
    else:
        emailBody = msg.get_payload(decode=True).decode(errors="ignore")


    recipient = parseaddr(emailFrom)[1]
    reply_subject = (
        emailSubject if (emailSubject or "").lower().startswith("re:") else f"Re: {emailSubject or ''}"
    )
    parent_message_id = msg.get("Message-Id")
    references = msg.get("References")
    if parent_message_id and references:
        references = f"{references} {parent_message_id}".strip()
    elif parent_message_id:
        references = parent_message_id


    response = emailValidatorLLM(msg)
    if response["reply_needed"]:
        response = generate_response(emailSubject, emailBody, emailFrom)

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
