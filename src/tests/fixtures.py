TEXT_NO_REGEX_EN = "Hi! How are you doing?"
TEXT_NO_REGEX_ES = "Hola! ¿Que tal lo llevas?"
TEXT_NO_REGEX_ZH = "嗨，情况如何"
TEXT_REGEX_EN = "We offer you 100K"
TEXT_NO_REGEX_UNKNOWN = ""

MESSAGE_IDENTIFIER = "2-NGY0ZGYxYjUtNDc0MS01ZGY0LTkzMjctYmIyMzZkYzZmNjkwXzAwMA=="
RESPONSE_CONVERSATIONS = {
    "elements": [
        {
            "backendUrn": f"urn:li:messagingThread:{MESSAGE_IDENTIFIER}",
            "participants": [{"com.linkedin.voyager.messaging.MessagingMember": {"miniProfile": {"firstName": "Foo"}}}],
        }
    ]
}


def _build_event_content(text):
    return {"eventContent": {"com.linkedin.voyager.messaging.event.MessageEvent": {"attributedBody": {"text": text}}}}


def build_conversation_response(texts):
    result = {"elements": []}
    for text in texts:
        result["elements"].append(_build_event_content(text))
    return result
