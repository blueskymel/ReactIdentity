# Enterprise AI Knowledge Platform  
### Azure AI Foundry + Python + React + Enterprise RAG Architecture

An enterprise-grade AI platform built using Microsoft Azure AI Foundry, Azure OpenAI, Python backend services, Azure AI Search, and React frontend.

This project focuses on building a production-ready enterprise knowledge platform that enables secure document ingestion, vector storage, intelligent retrieval, grounded response generation, evaluation pipelines, and guardrail enforcement using Microsoft’s modern Agent Framework ecosystem.

The goal is to simulate how enterprise consulting organizations build scalable AI platforms for customers using modern retrieval pipelines, agentic workflows, evaluation frameworks, and enterprise governance controls.

---

## Project Vision

Traditional AI applications typically follow a simple request-response pattern.

```text
User → Prompt → LLM → Response
```

Modern enterprise AI systems require significantly more architecture.

```text
Enterprise Documents
        ↓
Document Upload Pipeline
        ↓
Document Parsing
        ↓
Chunking Pipeline
        ↓
Embedding Generation
        ↓
Vector Storage
        ↓
Retrieval Pipeline
        ↓
Agent Reasoning
        ↓
Evaluation Pipeline
        ↓
Guardrails Pipeline
        ↓
Final Grounded Response
```

This project demonstrates how enterprise-grade AI systems should be designed using Microsoft Azure AI Foundry and modern Agent Framework architecture.

---

## Architecture Overview

```text
React Frontend
      ↓
Azure Front Door
      ↓
Azure API Management
      ↓
Python FastAPI Backend
      ↓
-------------------------------------------------
Document Ingestion Pipeline
-------------------------------------------------
Upload Document
      ↓
Document Parser
      ↓
Chunking Service
      ↓
Embedding Service
      ↓
Azure AI Search Vector Store
-------------------------------------------------
      ↓
-------------------------------------------------
Retrieval Pipeline
-------------------------------------------------
User Query
      ↓
Query Embedding
      ↓
Vector Search
      ↓
Relevant Document Retrieval
-------------------------------------------------
      ↓
-------------------------------------------------
Agent Runtime (Azure AI Foundry)
-------------------------------------------------
Context Injection
      ↓
Reasoning Agent
      ↓
Grounded Response Generation
-------------------------------------------------
      ↓
-------------------------------------------------
Evaluation Pipeline
-------------------------------------------------
Faithfulness Evaluation
Relevance Evaluation
Context Precision
Answer Quality
-------------------------------------------------
      ↓
-------------------------------------------------
Guardrails Pipeline
-------------------------------------------------
Prompt Injection Detection
Hallucination Detection
Safety Validation
Policy Compliance Checks
-------------------------------------------------
      ↓
Final Response
      ↓
Azure Monitor + Application Insights
```

---

## Core Features

## Software Architecture Principles

This project applies enterprise software engineering principles to AI platform development rather than treating AI workflows as simple scripts or prototypes.

The system is designed using SOLID principles to ensure maintainability, extensibility, and production readiness.

Applied principles:

### Single Responsibility Principle (SRP)

Each component has one clear responsibility.

Examples:

- UploadService → file persistence
- Parser → document text extraction
- Chunker → document segmentation
- EmbeddingService → vector generation
- VectorStore → vector persistence

---

### Open Closed Principle (OCP)

The system is open for extension without modifying existing code.

Examples:

New document parser support can be added without modifying pipeline code.

```text
BaseParser
      ↓
PDFParser
DOCXParser
TXTParser
```

---

### Dependency Inversion Principle (DIP)

High-level pipeline orchestration depends on abstractions rather than concrete implementations.

Example:

```text
DocumentIngestionPipeline
      ↓
BaseParser
BaseChunker
BaseEmbeddingService
```

This allows components to be swapped without changing orchestration logic.

### Document Ingestion Pipeline

Enterprise documents are uploaded and processed into searchable knowledge.

Supported document types:

- PDF
- DOCX
- TXT
- Markdown
- SharePoint Documents

Pipeline:

```text
Upload → Parse → Chunk → Embed → Store Vector
```

---

### Vector Storage

Document chunks are converted into embeddings and stored in vector database.

Technology:

- Azure AI Search
- Vector Search
- Hybrid Search

Embedding models:

- text-embedding-3-small
- text-embedding-3-large

---

### Retrieval Pipeline (RAG)

User questions are transformed into embeddings and matched against stored vectors.

Process:

```text
Question
    ↓
Embedding Generation
    ↓
Similarity Search
    ↓
Top K Retrieval
    ↓
Context Injection
```

Capabilities:

- Semantic Search
- Hybrid Search
- Context Retrieval
- Source Citation

---

### Agent Reasoning Layer

Azure AI Foundry agent processes retrieved context and generates grounded answers.

Responsibilities:

- Grounded response generation
- Multi-step reasoning
- Tool calling
- Enterprise workflow execution

Models:

- GPT-4o
- GPT-4o-mini

---

### Evaluation Pipeline

All responses are evaluated before returning to user.

Evaluation criteria:

- Faithfulness
- Answer relevance
- Context precision
- Answer completeness
- Groundedness verification

Purpose:

Ensure generated answers are trustworthy and aligned with source documents.

---

### Guardrails Pipeline

Enterprise AI systems require protection against unsafe outputs.

Guardrails include:

- Prompt injection detection
- Hallucination detection
- Restricted content filtering
- PII detection
- Policy compliance validation

Purpose:

Prevent unsafe or ungrounded AI responses.

---

### Enterprise Security

Authentication and authorization handled through enterprise identity.

Security stack:

- Microsoft Entra ID
- RBAC
- Managed Identity
- Secure API Gateway
- Role-based document access

---

### Observability

Production monitoring for enterprise AI workloads.

Tracked metrics:

- Prompt execution logs
- Token usage
- Latency monitoring
- Tool execution logs
- Failure tracing
- Retrieval accuracy
- Model cost monitoring

Services:

- Azure Monitor
- Azure Application Insights

---

## Technology Stack

## Design Patterns

The project follows enterprise software design patterns to support extensibility and cloud provider independence.

### Strategy Pattern

Used when multiple interchangeable implementations exist.

Examples:

```text
BaseParser
      ↓
PDFParser
DOCXParser
MarkdownParser
```

```text
BaseChunker
      ↓
SemanticChunker
RecursiveChunker
```

```text
BaseEmbeddingService
      ↓
AzureOpenAIEmbeddingService
OpenAIEmbeddingService
LocalEmbeddingService
```

---

### Factory Pattern

Responsible for selecting implementations dynamically.

Examples:

```text
ParserFactory → returns parser based on file type

ChunkerFactory → returns chunker based on strategy
```

This avoids hardcoded dependencies.

---

### Pipeline Pattern

The entire system follows staged processing architecture.

```text
Upload
      ↓
Parse
      ↓
Chunk
      ↓
Embed
      ↓
Store Vector
      ↓
Retrieve
      ↓
Evaluate
      ↓
Guardrails
```

Each stage operates independently.

---

### Adapter Pattern (Planned)

Used to abstract cloud-specific services.

Examples:

```text
Azure AI Search Adapter

Pinecone Adapter

Qdrant Adapter
```

Allows future vector store portability.

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- MSAL React

---

### Backend

- Python 3.13
- FastAPI
- AsyncIO
- Pydantic

---

### AI Platform

- Azure AI Foundry
- Azure OpenAI
- GPT-4o
- GPT-4o-mini
- Microsoft Agent Framework

---

### Document Processing

- PyPDF
- Python-docx
- Text Extraction Services

---

### Vector Storage

- Azure AI Search
- Embedding Models

---

### Cloud Infrastructure

- Azure API Management
- Azure Functions
- Azure Blob Storage
- Azure Monitor
- Application Insights

---

## End-to-End Request Flow

User uploads enterprise documents.

```text
Document Upload
      ↓
Parse Document Content
      ↓
Split Into Chunks
      ↓
Generate Embeddings
      ↓
Store in Azure AI Search
```

User asks question.

```text
User Question
      ↓
Generate Query Embedding
      ↓
Retrieve Relevant Chunks
      ↓
Inject Context into Agent
      ↓
Generate Response
      ↓
Evaluate Response Quality
      ↓
Run Guardrails Validation
      ↓
Return Final Response
```

---

## Repository Structure

```text
project-root/

frontend/
  react-app/

backend/

  ingestion/

      parsers/
          base_parser.py
          pdf_parser.py
          docx_parser.py
          parser_factory.py

      chunkers/
          base_chunker.py
          recursive_chunker.py
          semantic_chunker.py
          chunker_factory.py

      upload_service.py
      document_ingestion_pipeline.py

  embeddings/
      base_embedding_service.py
      azure_openai_embedding.py

  search/
      base_vector_store.py
      azure_ai_search.py

  agents/
      rag_agent.py

  evaluation/
      evaluator.py

  guardrails/
      validator.py

  api/
      main.py

  tests/
      test_ingestion.py

  config/
      settings.py
```

---

## Enterprise Design Principles

This platform follows enterprise AI engineering principles.

Design principles:

- Security First
- Grounded Responses Only
- Retrieval Before Generation
- Observable AI Execution
- Evaluation Before Delivery
- Guardrails Before Response
- Enterprise Authentication
- Scalable Cloud-Native Deployment
- Cost Optimization

---

## Future Enhancements

Planned roadmap:

- Multi-agent orchestration
- Model Context Protocol (MCP) integration
- Agent memory persistence
- Streaming responses
- Multi-tenant deployment
- Continuous evaluation framework
- Advanced guardrails engine
- Human approval workflows
- CI/CD deployment pipelines

---

## Purpose

This project explores modern enterprise AI architecture patterns aligned with Microsoft’s evolving AI roadmap.

Focus areas:

- Enterprise AI Platforms
- Azure AI Foundry
- Retrieval Augmented Generation (RAG)
- Vector Search Architecture
- Agentic AI Systems
- Evaluation Frameworks
- Guardrails Architecture
- Production AI Engineering

---

## Status

Currently under active development.

Version: v2 Enterprise RAG Architecture

Architecture Phase: Document Pipeline → Retrieval → Evaluation → Guardrails