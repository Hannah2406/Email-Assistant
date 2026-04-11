"""Claude: classify whether a reply is needed and draft responses."""

from __future__ import annotations


def build_anthropic_client(api_key: str):
    # TODO: return an Anthropic client configured with ANTHROPIC_API_KEY
    raise NotImplementedError


def classify_needs_reply(client, model: str, email_payload: dict):
    # TODO: call Claude with your classification prompt; return structured result (needs_reply: bool, rationale, etc.)
    raise NotImplementedError


def draft_reply(client, model: str, email_payload: dict, classification_context: dict | None):
    # TODO: call Claude to draft a reply when classify_needs_reply is true
    raise NotImplementedError
