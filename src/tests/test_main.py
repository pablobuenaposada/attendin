from unittest.mock import ANY, call, patch

import pytest

from constants import DEFAULT_ANSWERS
from main import main
from tests.fixtures import (
    MESSAGE_IDENTIFIER,
    RESPONSE_CONVERSATIONS,
    TEXT_NO_REGEX_EN,
    TEXT_NO_REGEX_ES,
    TEXT_NO_REGEX_UNKNOWN,
    TEXT_NO_REGEX_ZH,
    TEXT_REGEX_EN,
    build_conversation_response,
)


class TestMain:
    @pytest.mark.parametrize(
        "conversation, expected_send_message_calls",
        (
            # 1 message and it doesn't match any regex, english
            (
                build_conversation_response([TEXT_NO_REGEX_EN]),
                [
                    call().send_message(
                        DEFAULT_ANSWERS["en"],
                        conversation_urn_id=MESSAGE_IDENTIFIER,
                    )
                ],
            ),
            # 1 message and it doesn't match any regex, spanish
            (
                build_conversation_response([TEXT_NO_REGEX_ES]),
                [
                    call().send_message(
                        DEFAULT_ANSWERS["es"],
                        conversation_urn_id=MESSAGE_IDENTIFIER,
                    )
                ],
            ),
            # 1 message but matches a regex
            (
                build_conversation_response([TEXT_REGEX_EN]),
                [],
            ),
            # 2 messages
            (
                build_conversation_response([TEXT_NO_REGEX_EN, TEXT_REGEX_EN]),
                [],
            ),
            # unknown message language
            (
                build_conversation_response([TEXT_NO_REGEX_UNKNOWN]),
                [],
            ),
            # no answer set up for the language detected
            (
                build_conversation_response([TEXT_NO_REGEX_ZH]),
                [],
            ),
        ),
    )
    def test_defaults(self, conversation, expected_send_message_calls):
        """
        Execute the main behaviour with default args
        """
        with patch("main.Linkedin") as m_linkedin:
            m_linkedin.return_value.get_conversations.return_value = RESPONSE_CONVERSATIONS
            m_linkedin.return_value.get_conversation.return_value = conversation
            main(ANY, ANY)  # any username and password

        assert m_linkedin._mock_mock_calls[0:3] == [
            call(ANY, ANY),
            call().get_conversations(),
            call().get_conversation(MESSAGE_IDENTIFIER),
        ]
        assert m_linkedin._mock_mock_calls[3:] == expected_send_message_calls

    @pytest.mark.parametrize(
        "args, conversation, expected_send_message_calls",
        (
            # changing the regexes
            (
                {"username": ANY, "password": ANY, "regexes": [TEXT_NO_REGEX_EN[0:3]]},
                build_conversation_response([TEXT_NO_REGEX_EN]),
                [],
            ),
            # changing the answers
            (
                {"username": ANY, "password": ANY, "answers": {"en": "test"}},
                build_conversation_response([TEXT_NO_REGEX_EN]),
                [
                    call().send_message(
                        "test",
                        conversation_urn_id=ANY,
                    )
                ],
            ),
        ),
    )
    def test_optional_args(self, args, conversation, expected_send_message_calls):
        """
        Execute the main behaviour with optional args
        """
        with patch("main.Linkedin") as m_linkedin:
            m_linkedin.return_value.get_conversations.return_value = RESPONSE_CONVERSATIONS
            m_linkedin.return_value.get_conversation.return_value = conversation
            main(**args)

        assert m_linkedin._mock_mock_calls[0:3] == [
            call(ANY, ANY),
            call().get_conversations(),
            call().get_conversation(MESSAGE_IDENTIFIER),
        ]
        assert m_linkedin._mock_mock_calls[3:] == expected_send_message_calls
