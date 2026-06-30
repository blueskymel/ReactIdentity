from abc import ABC, abstractmethod
from typing import List


class BaseEmbeddingService(ABC):

    @abstractmethod
    async def generate_embedding(
        self,
        text: str
    ) -> List[float]:
        pass
