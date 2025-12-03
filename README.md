BoardRAG — Remote AI Assistant for Business Reports
A 15-Day Full-Stack GenAI Project (Beginner → Advanced)
Day 1 Completed Successfully
🎯 Project Overview

BoardRAG is a Retrieval-Augmented Generation (RAG) system designed for business meetings and executive use-cases.
A presenter uploads files such as:

Power BI dashboards

Tableau exports

PDF reports

PPT presentations

Excel sheets

Images/screenshots

Board members can then ask questions in a chat interface, and the system retrieves relevant information using:

OCR

Embedding models

Vector search (FAISS)

LLM-based answer generation

The system supports remote usage, authentication, cloud storage, and multi-user collaboration.

## Day 3 — Ingestion Pipeline (PDF, PPTX, Images, Excel)

Today I implemented the ingestion subsystem of BoardRAG, which is responsible for extracting content from files uploaded by presenters. This includes:

- PDF processing using pdfminer
- PPTX slide extraction using python-pptx
- OCR text extraction using OpenCV + Tesseract
- Excel text extraction using pandas
- Metadata generation for each extracted block

Ingestion is the foundational layer of a RAG system because incorrect or incomplete extraction directly affects retrieval accuracy. This module now generates clean text, structured data, and metadata that will feed into the chunking and embedding pipeline on Day 4.
