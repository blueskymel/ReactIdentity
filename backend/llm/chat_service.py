from backend.llm.azure_openai_client import (
    AzureOpenAIClient
)

from backend.config.settings import (

    AZURE_OPENAI_CHAT_DEPLOYMENT,

    CHAT_TEMPERATURE,

    CHAT_MAX_TOKENS
)
from backend.common.logger import (
    logger
)
from backend.models.chat.chat_request_model import ChatRequest


class ChatService:

    def __init__(self):

        self.client = (
            AzureOpenAIClient.create()
        )

    def generate_response(
        self,
        request: ChatRequest
    ) -> str:

        prompt = f"""
You are an enterprise assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, say:

'I cannot find that information in the provided documents.'

Context:
{request.context}

Question:
{request.question}
"""

        logger.info(
            "Calling Azure OpenAI",
            extra={
                "deployment": AZURE_OPENAI_CHAT_DEPLOYMENT,
                "temperature": CHAT_TEMPERATURE,
                "max_tokens": CHAT_MAX_TOKENS,
                "operation": "chat_completion"
            }
        )

        response = (
            self.client.chat.completions.create(

                model=AZURE_OPENAI_CHAT_DEPLOYMENT,

                temperature=CHAT_TEMPERATURE,

                max_tokens=CHAT_MAX_TOKENS,

                messages=[
                    {
                        "role": "system",

                        "content":
                        "You are a helpful enterprise assistant."
                    },

                    {
                        "role": "user",

                        "content": prompt
                    }
                ]
            )
        )

        content = (
            response
            .choices[0]
            .message
            .content
        )

        if content is None:

            raise ValueError(
                "No response returned"
            )

        return content
