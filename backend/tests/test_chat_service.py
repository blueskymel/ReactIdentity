import asyncio

import pytest

from backend.llm.chat_service import (
    ChatService
)

from backend.models.chat.chat_request_model import (
    ChatRequest
)


@pytest.mark.integration
def test_chat():

    service = ChatService()

    result = asyncio.run(
        service.generate_response(
            ChatRequest(
                question=
                "How long should customer data be stored?",

                context=
                "Customer personal data must be retained for 7 years according to company policy."
            )
        )
    )

    print(result)


if __name__ == "__main__":

    test_chat()
