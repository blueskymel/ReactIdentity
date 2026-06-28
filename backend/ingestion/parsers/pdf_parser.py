from pypdf import PdfReader
from backend.ingestion.parsers.base_parser import BaseParser


class PDFParser(BaseParser):

    def parse(self, file_path: str) -> str:

        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                pages.append(extracted)

        return "\n".join(pages)