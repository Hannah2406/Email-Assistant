"""Connect to mail servers with EMAIL_ADDRESS + EMAIL_APP_PASSWORD."""

import imaplib
import smtplib

def connect_imap(settings):
    client = imaplib.IMAP4_SSL(settings.imap_host, settings.imap_port)
    client.login(settings.email, settings.email_password)
    return client


def connect_smtp(settings):
    server = smtplib.SMTP(settings.smtp_host, settings.smtp_port)
    server.starttls()
    server.login(settings.email, settings.email_password)
    return server
