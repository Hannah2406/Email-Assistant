"""IMAP: fetch messages. SMTP: send replies."""

from __future__ import annotations


def fetch_new_message(imap):
    imap.select("INBOX")
    status, data = imap.search(None, "ALL")
    mail_ids = data[0].split()
    latest_id = mail_ids[-1]
    status, msg_data = imap.fetch(latest_id, "(RFC822)")
    return latest_id, msg_data



def send_message(smtp, from_addr: str, to_addrs: list[str], message_bytes: bytes):
    # TODO: sendmail / send_message for a drafted MIME reply (respect threading headers In-Reply-To, References)
    raise NotImplementedError
