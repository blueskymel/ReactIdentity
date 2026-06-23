from backend.ingestion.parsers.docx_parser import DOCXParser
from backend.ingestion.parsers.pdf_parser import PDFParser


class ParserFactory:

    @staticmethod
    def get_parser(extension: str):

        parsers = {
            ".pdf": PDFParser(),
            ".docx": DOCXParser()
        }

        return parsers.get(extension)
