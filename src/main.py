import argparse
import re

from langdetect import detect, lang_detect_exception
from linkedin_api import Linkedin

from constants import DEFAULT_ANSWERS, DEFAULT_REGEXES


def main(username, password, regexes=DEFAULT_REGEXES, answers=DEFAULT_ANSWERS):
    linkedin = Linkedin(username, password)

    for conversation in linkedin.get_conversations()["elements"][:10]:
        conversation_urn_id = conversation["backendUrn"].split(":")[3]
        requester = conversation["participants"][0]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"][
            "firstName"
        ]
        print(f"checking conversation {conversation_urn_id} from {requester}", end="")
        messages = linkedin.get_conversation(conversation_urn_id)["elements"]
        if len(messages) == 1:  # means conversation has been never replied
            first_message = messages[0]["eventContent"]["com.linkedin.voyager.messaging.event.MessageEvent"][
                "attributedBody"
            ]["text"]
            if all(not re.search(regex, first_message) for regex in regexes):
                # if no regex is found then we send the corresponding message
                try:
                    message_language = detect(first_message)
                except lang_detect_exception.LangDetectException:
                    continue  # if no language detected this conversation is skipped
                try:
                    linkedin.send_message(answers[message_language], conversation_urn_id=conversation_urn_id)
                    print(" AUTO REPLIED!", end="")
                except KeyError:
                    continue  # if there's no answer set up for the language detected conversation is skipped
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--regexes", action="append")
    parser.add_argument("--answers", action="append")
    args = parser.parse_args()
    # delete values with none or ""
    input = {key: value for key, value in args.__dict__.items() if not value == [""] or value is None}
    main(**input)
