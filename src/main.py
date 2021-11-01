import argparse
import re

from langdetect import detect, lang_detect_exception
from linkedin_api import Linkedin

from constants import DEFAULT_ANSWERS, DEFAULT_REGEXES


def main(username, password, regexes=DEFAULT_REGEXES, answers=DEFAULT_ANSWERS):
    linkedin = Linkedin(username, password)

    for conversation in linkedin.get_conversations()["elements"]:
        conversation_urn_id = conversation["backendUrn"].split(":")[2]
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
                except KeyError:
                    continue  # if there's no answer set up for the language detected conversation is skipped


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--regexes", action="append")
    parser.add_argument("--answers", action="append")
    args = parser.parse_args()
    input = {key: value for key, value in args.__dict__.items() if value is not None}  # delete values with none
    main(**input)
