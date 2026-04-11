"""Connect to mail servers with EMAIL_ADDRESS + EMAIL_APP_PASSWORD."""

from __future__ import annotations


def connect_imap(settings):
    # TODO: return an imaplib.IMAP4_SSL (or STARTTLS) client logged in with settings email + app password
    raise NotImplementedError


def connect_smtp(settings):
    # TODO: return an smtplib.SMTP (or SMTP_SSL) session logged in and ready to send
    raise NotImplementedError
