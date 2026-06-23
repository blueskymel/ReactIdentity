from typing import List

from openai import AzureOpenAI

from backend.embeddings.base_embedding_service import (
    BaseEmbeddingService
)

from backend.config.settings import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_EMBEDDING_MODEL
)


class AzureOpenAIEmbeddingService(
    BaseEmbeddingService
):

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=AZURE_OPENAI_API_KEY,
            api_version="2024-02-01",
            azure_endpoint=AZURE_OPENAI_ENDPOINT
        )

    def generate_embedding(
        self,
        text: str
    ) -> List[float]:

        response = self.client.embeddings.create(
            model=AZURE_OPENAI_EMBEDDING_MODEL,
            input=text
        )

        return response.data[0].embedding
