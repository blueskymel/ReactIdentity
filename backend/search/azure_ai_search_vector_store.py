from azure.core.credentials import AzureKeyCredential

from azure.search.documents import SearchClient

from backend.search.base_vector_store import (
    BaseVectorStore
)

from backend.models.vector_document import (
    VectorDocument
)

from backend.config.settings import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
    AZURE_SEARCH_INDEX
)


class AzureAISearchVectorStore(
    BaseVectorStore
):

    def __init__(self):

        self.client = SearchClient(
            endpoint=AZURE_SEARCH_ENDPOINT,

            index_name=AZURE_SEARCH_INDEX,

            credential=AzureKeyCredential(
                AZURE_SEARCH_KEY
            )
        )

    def store(
        self,
        document: VectorDocument
    ) -> None:

        payload = {
            "id": document.id,
            "content": document.content,
            "embedding": document.embedding,
            "document_name": document.document_name,
            "chunk_index": document.chunk_index
        }

        try:

            result = self.client.upload_documents(
                documents=[payload]
            )

            print(result)

        except Exception as ex:

            raise RuntimeError(
                f"Azure AI Search upload failed: {ex}"
            )