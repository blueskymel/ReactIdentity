from openai import AzureOpenAI

from backend.config.settings import (

    AZURE_OPENAI_API_KEY,

    AZURE_OPENAI_ENDPOINT,

    AZURE_OPENAI_API_VERSION
)


class AzureOpenAIClient:

    @staticmethod
    def create() -> AzureOpenAI:

        return AzureOpenAI(

            api_key=AZURE_OPENAI_API_KEY,

            api_version=AZURE_OPENAI_API_VERSION,

            azure_endpoint=AZURE_OPENAI_ENDPOINT
        )