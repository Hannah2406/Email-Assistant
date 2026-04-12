"""Application entry point."""
from email_assistant.config import settings
from email_assistant.gmail import connect_imap
from email_assistant.gmail.client import fetch_new_message
from email_assistant.llm.OpenRouter import generate_response

import email

def main():
    imap = connect_imap(settings)

    latest_id, msg_data = fetch_new_message(imap)

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


    
    response = generate_response(emailSubject, emailBody, emailFrom)
    print(response)

    imap.logout()
    


if __name__ == "__main__":
    main()
