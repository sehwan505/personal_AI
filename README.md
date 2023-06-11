# Personal AI: GPT PDF Reader using Pinecone

## Project Description

This project provides an AI solution that uses GPT and Pinecone to read and process PDF files. This opens up new possibilities in terms of large scale document processing, information extraction, text summarization, and more. 

## Features

- PDF document reading and parsing.
- Text extraction from PDFs.
- Text processing and understanding using GPT.
- Integration with Pinecone for efficient information retrieval.

## Prerequisites

The project requires the following dependencies:

- Python 3.11
- GPT
- Pinecone
- OpenAI
- Langchain

## Installation

To install this project, follow these steps:

```bash
git clone https://github.com/sehwan505/personal_AI.git
cd personal_AI
poetry install
cd personal_ai
poetry run uvicorn main:app --host 0.0.0.0 --port 80
```
