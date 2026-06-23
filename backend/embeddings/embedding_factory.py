from backend.embeddings.azure_openai_embedding import (
    AzureOpenAIEmbeddingService
)


class EmbeddingFactory:

    @staticmethod
    def get_embedding_service():

        return AzureOpenAIEmbeddingService()
