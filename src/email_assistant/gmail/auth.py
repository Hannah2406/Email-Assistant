"""Connect to mail servers with EMAIL_ADDRESS + EMAIL_APP_PASSWORD."""

import imaplib
import smtplib


def _port(value, default: int) -> int: 
    # since env variables are strings, we need to convert to int for port
    if value is None or value == "":
        return default
    return int(value)


def connect_imap(settings):
    port = _port(settings.imap_port, 993)
    # create encrypted imap connection + authenticate with app pswd
    client = imaplib.IMAP4_SSL(settings.imap_host, port)
    client.login(settings.email, settings.email_password)
    return client


def connect_smtp(settings):
    port = _port(settings.smtp_port, 587)
    # open SMTP 
    server = smtplib.SMTP(settings.smtp_host, port)
    server.starttls()
    server.login(settings.email, settings.email_password)
    return server
