"""Gmail API: list and fetch messages for polling."""

from __future__ import annotations


def build_gmail_service(credentials):
    # TODO: construct a Gmail API service resource from google credentials
    raise NotImplementedError


def fetch_messages_since(service, since_internal_date_ms: int | None):
    # TODO: list message ids / threads updated after the given internalDate (or full sync strategy)
    raise NotImplementedError


def get_message_rfc822(service, message_id: str):
    # TODO: return raw RFC822 or parsed structure suitable for Claude (headers + body text)
    raise NotImplementedError
