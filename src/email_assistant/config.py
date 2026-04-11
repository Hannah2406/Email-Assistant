"""Load application settings from environment variables."""
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
    anthropic_api_key: str
    claude_model: str

def load_settings():
    settings = Settings(
        email=os.getenv("EMAIL_ADDRESS"),
        email_password=os.getenv("EMAIL_APP_PASSWORD"),
        imap_host=os.getenv("IMAP_HOST"),
        imap_port=int(os.getenv("IMAP_PORT")),
        smtp_host=os.getenv("SMTP_HOST"),
        smtp_port=int(os.getenv("SMTP_PORT")),
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
        claude_model=os.getenv("CLAUDE_MODEL"),
    )
    return settings

settings = load_settings()
