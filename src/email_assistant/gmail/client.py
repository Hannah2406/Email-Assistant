"""IMAP: fetch messages. SMTP: send replies."""

from __future__ import annotations

from email.message import EmailMessage
from email import message_from_bytes
from email.policy import SMTP as SMTP_POLICY


def fetch_new_message(imap):
    imap.select("INBOX")
    _, data = imap.search(None, "ALL")
    mail_ids = data[0].split()
    latest_id = mail_ids[-1]
    _, msg_data = imap.fetch(latest_id, "(RFC822)")
    return latest_id, msg_data


def compose_text_email(
    from_addr: str,
    to_addrs: list[str],
    subject: str,
    body: str,
    *,
    in_reply_to: str | None = None,
    references: str | None = None,
) -> bytes:
    """Build a simple UTF-8 plain-text message. For threading, pass Message-Id values from the email you reply to."""
    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = ", ".join(to_addrs)
    msg["Subject"] = subject
    if in_reply_to:
        msg["In-Reply-To"] = in_reply_to
    if references:
        msg["References"] = references
    msg.set_content(body, subtype="plain", charset="utf-8")
    return msg.as_bytes(policy=SMTP_POLICY)


def send_message(smtp, from_addr: str, to_addrs: list[str], message_bytes: bytes) -> None:
    """Send an RFC822 message produced by compose_text_email or another MIME builder."""
    msg = message_from_bytes(message_bytes)
    smtp.send_message(msg, from_addr=from_addr, to_addrs=to_addrs)
