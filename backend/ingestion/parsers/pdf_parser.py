from pypdf import PdfReader

from backend.ingestion.parsers.base_parser import BaseParser


class PDFParser(BaseParser):

    def parse(self, file_path: str) -> str:

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text
