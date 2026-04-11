"""Main agent loop: poll inbox over IMAP, classify with Claude, send drafts over SMTP when needed."""


def run_once(settings, imap, smtp, anthropic_client):
    # TODO: one iteration — fetch new mail via IMAP, classify, draft replies, send via SMTP when appropriate
    raise NotImplementedError


def run_forever(settings, imap, smtp, anthropic_client):
    # TODO: sleep MAIL_POLL_INTERVAL_SECONDS between iterations; handle signals gracefully if desired
    raise NotImplementedError
