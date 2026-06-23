from docx import Document

from backend.ingestion.parsers.base_parser import BaseParser


class DOCXParser(BaseParser):

    def parse(self, file_path: str) -> str:

        doc = Document(file_path)

        return "\n".join(
            paragraph.text for paragraph in doc.paragraphs
        )
        
