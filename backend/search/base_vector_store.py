from abc import ABC, abstractmethod
from typing import List

from backend.models.vector_document import (
    VectorDocument
)


class BaseVectorStore(ABC):

    @abstractmethod
    async def store(
        self,
        document: VectorDocument
    ) -> None:
        pass


    @abstractmethod
    async def search(
        self,
        query: str,
        embedding: List[float],
        top_k: int = 3
    ) -> List[VectorDocument]:
        pass

    @abstractmethod
    async def delete_by_document_name(
        self,
        document_name: str
    ) -> None:
        pass