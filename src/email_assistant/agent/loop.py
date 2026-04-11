"""Main agent loop: poll Gmail, classify with Claude, draft replies when needed."""


def run_once(settings, gmail_service, anthropic_client):
    # TODO: one iteration — fetch new mail, classify, enqueue or draft replies
    raise NotImplementedError


def run_forever(settings, gmail_service, anthropic_client):
    # TODO: sleep GMAIL_POLL_INTERVAL_SECONDS between iterations; handle signals gracefully if desired
    raise NotImplementedError
