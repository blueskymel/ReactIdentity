from backend.ingestion.document_ingestion_pipeline import DocumentProcessor


def test_document_processor_can_be_created():
    processor = DocumentProcessor(chunking_strategy="semantic")

    assert processor.chunking_strategy == "semantic"