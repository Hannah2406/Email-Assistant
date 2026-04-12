"""Load application settings from environment variables."""
from dotenv import load_dotenv
load_dotenv()
import os
from dataclasses import dataclass

@dataclass
class Settings:
    email: str
    email_password: str
    imap_host: str
    imap_port: int
    smtp_host: str
    smtp_port: int
    openai_router_key: str

def load_settings():
    settings = Settings(
        email=os.getenv("EMAIL_ADDRESS"),
        email_password=os.getenv("EMAIL_APP_PASSWORD"),
        imap_host=os.getenv("IMAP_HOST"),
        imap_port=os.getenv("IMAP_PORT"),
        smtp_host=os.getenv("SMTP_HOST"),
        smtp_port=os.getenv("SMTP_PORT"),
        openai_router_key=os.getenv("OPENAI_ROUTER_KEY"),
    )
    return settings

settings = load_settings()
