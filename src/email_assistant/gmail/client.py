"""IMAP: fetch messages. SMTP: send replies."""

from __future__ import annotations


def fetch_messages_since(imap, since_uid: int | None):
    # TODO: SEARCH UNSEEN or SINCE / UID range; return a list of message identifiers (UIDs or indices) for the agent loop
    raise NotImplementedError


def get_message_rfc822(imap, message_id: str):
    # TODO: FETCH the message (BODY.PEEK[] or RFC822); return bytes or parsed email.message.EmailMessage for Claude
    raise NotImplementedError


def send_message(smtp, from_addr: str, to_addrs: list[str], message_bytes: bytes):
    # TODO: sendmail / send_message for a drafted MIME reply (respect threading headers In-Reply-To, References)
    raise NotImplementedError
