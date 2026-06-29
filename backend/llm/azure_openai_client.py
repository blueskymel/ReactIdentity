from openai import AsyncAzureOpenAI

from backend.config.settings import (

    AZURE_OPENAI_API_KEY,

    AZURE_OPENAI_ENDPOINT,

    AZURE_OPENAI_API_VERSION
)


class AzureOpenAIClient:

    @staticmethod
    def create() -> AsyncAzureOpenAI:

        return AsyncAzureOpenAI(

            api_key=AZURE_OPENAI_API_KEY,

            api_version=AZURE_OPENAI_API_VERSION,

            azure_endpoint=AZURE_OPENAI_ENDPOINT
        )
