from typing import List

from azure.search.documents.models import (
    VectorizedQuery
)

from azure.core.credentials import (
    AzureKeyCredential
)

from azure.search.documents.aio import (
    SearchClient
)

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

from backend.common.logger import (
    logger
)


AZURE_SEARCH_VECTOR_FIELD = "embedding"


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


    def _map_search_result(

        self,

        result: dict

    ) -> VectorDocument:

        return VectorDocument(

            id=result["id"],

            content=result["content"],

            embedding=[],

            document_name=result["document_name"],

            chunk_index=result["chunk_index"],

            metadata={
                "score": result.get(
                    "@search.score",
                    0
                )
            }
        )


    async def store(

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

            logger.info(
                "Calling Azure AI Search",
                extra={
                    "operation": "upload_documents",
                    "index": AZURE_SEARCH_INDEX,
                    "document_name": document.document_name,
                    "chunk_index": document.chunk_index,
                    "document_count": 1
                }
            )

            result = await self.client.upload_documents(
                documents=[payload]
            )

            if not all(

                item.succeeded

                for item in result
            ):

                logger.error(
                    "Azure Search document upload failed",
                    extra={
                        "document_name": document.document_name
                    }
                )

                raise RuntimeError(
                    "Document upload failed"
                )

            logger.info(
                "Azure Search document upload succeeded",
                extra={
                    "document_name": document.document_name
                }
            )

        except Exception:

            logger.exception(
                "Azure Search upload failed"
            )

            raise


    async def search(

        self,

        query: str,

        embedding: List[float],

        top_k: int = 3

    ) -> List[VectorDocument]:

        vector_query = VectorizedQuery(

            vector=embedding,

            k_nearest_neighbors=top_k,

            fields=AZURE_SEARCH_VECTOR_FIELD
        )

        logger.info(
            "Calling Azure AI Search",
            extra={
                "operation": "vector_search",
                "index": AZURE_SEARCH_INDEX,
                "top_k": top_k,
                "embedding_dimensions": len(embedding)
            }
        )

        results = await self.client.search(

            search_text=query,

            vector_queries=[vector_query],

            top=top_k
        )

        documents = []

        async for result in results:

            documents.append(

                self._map_search_result(
                    result
                )
            )

        return documents


    async def delete_by_document_name(

        self,

        document_name: str

    ) -> None:

        logger.info(
            "Calling Azure AI Search",
            extra={
                "operation": "search_documents_for_delete",
                "index": AZURE_SEARCH_INDEX,
                "document_name": document_name
            }
        )

        safe_document_name = (

            document_name.replace(
                "'",
                "''"
            )
        )

        results = await self.client.search(

            search_text="*",

            filter=f"document_name eq '{safe_document_name}'"
        )

        docs_to_delete = []

        async for result in results:

            docs_to_delete.append({

                "id": result["id"]
            })


        if docs_to_delete:

            logger.info(
                "Calling Azure AI Search",
                extra={
                    "operation": "delete_documents",
                    "index": AZURE_SEARCH_INDEX,
                    "document_name": document_name,
                    "document_count": len(docs_to_delete)
                }
            )

            await self.client.delete_documents(
                documents=docs_to_delete
            )

            logger.info(
                "Documents deleted",
                extra={
                    "count": len(docs_to_delete)
                }
            )