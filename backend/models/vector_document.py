from dataclasses import dataclass
from typing import List, Dict


@dataclass
class VectorDocument:

    id: str

    content: str

    embedding: List[float]

    document_name: str

    chunk_index: int

    metadata: Dict[str, str]