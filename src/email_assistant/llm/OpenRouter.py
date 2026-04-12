"""Claude: classify whether a reply is needed and draft responses."""

from __future__ import annotations
from openai import OpenAI
from email_assistant.config import settings


def get_llm_client():
    return OpenAI(
    api_key=settings.openai_router_key,
    base_url="https://openrouter.ai/api/v1")

def generate_response(emailSubject, emailBody, emailFrom):
    client = get_llm_client()

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages = [
            {
                "role": "system",
                "content": "you are a very sad ittle kid who doesnt know anything"
            },
            {
                "role": "user",
                "content": "what is the meaning of life?"
            }
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

def build_anthropic_client(api_key: str):
    # TODO: return an Anthropic client configured with ANTHROPIC_API_KEY
    raise NotImplementedError


def classify_needs_reply(client, model: str, email_payload: dict):
    # TODO: call Claude with your classification prompt; return structured result (needs_reply: bool, rationale, etc.)
    raise NotImplementedError


def draft_reply(client, model: str, email_payload: dict, classification_context: dict | None):
    # TODO: call Claude to draft a reply when classify_needs_reply is true
    raise NotImplementedError
