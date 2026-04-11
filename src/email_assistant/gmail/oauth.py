"""Gmail OAuth2 flow (authorization URL, token exchange, refresh)."""


def build_authorization_url():
    # TODO: return the Google OAuth consent URL for the Gmail scopes you need
    raise NotImplementedError


def exchange_code_for_tokens(authorization_code: str):
    # TODO: exchange the auth code for access + refresh tokens; persist via GMAIL_TOKEN_PATH
    raise NotImplementedError


def load_credentials():
    # TODO: load stored tokens from disk; refresh if expired
    raise NotImplementedError
