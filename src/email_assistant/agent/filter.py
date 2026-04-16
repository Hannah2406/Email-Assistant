from email_assistant.llm.OpenRouter import emailValidatorLLM

def getEmailBody():
    emailBody = ""

    if msg.is_multipart():
        for part in msg.get_payload():
            if part.get_content_type() == "text/plain":
                emailBody = part.get_payload(decode=True).decode(errors="ignore")
                break
    else:
        emailBody = msg.get_payload(decode=True).decode(errors="ignore")
    return emailBody

def getEmailAddress(email):
    if not from_header or not isinstance(from_header, str):
        return None
    s = from_header.strip()
    m = re.search(r"<([^<>]+@[^<>]+)>", s)
    if m:
        return m.group(1).strip()
    m = re.search(r"\b([\w.+-]+@[\w.-]+\.[a-z]{2,})\b", s, re.IGNORECASE)
    return m.group(1).strip() if m else None

def getLinkCount(email):
    return len(re.findall(r"https?://\S+", body or ""))

def emailValidator(email):
    address = getEmailAddress(email["FROM"])
    emailBody = getEmailBody(email)
    links = getLinkCount(emailBody)
    subject = email["SUBJECT"]
    hasUnsubscribe = "unsubscribe" in emailBody.lower()
    emailLength = len(emailBody.strip())
    isNoReply = "no-reply" in address.lower() or "noreply" in address.lower()

    data = {
        "from": address,
        "subject": subject,
        "num_links": links,
        "has_unsubscribe": hasUnsubscribe,
        "is_no_reply": isNoReply,
        "email_length": emailLength,
        "body_preview": bodyPreview
    }

    if is_no_reply or (num_links > 8 and has_unsubscribe) or (mailLength < 30 and links > 2):
        return False

    response = emailValidatorLLM(data)
    return response
    