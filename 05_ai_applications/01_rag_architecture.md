---
title: "RAG: Retrieval Augmented Generation"
description: "Giving LLMs access to private data."
---

# RAG Architecture

LLMs have a knowledge cutoff. They don't know your private emails or company documents. RAG fixes this.

## How it works

1.  **Ingestion**: Split your documents into chunks.
2.  **Embedding**: Convert chunks into vectors using an Embedding Model (e.g., OpenAI, SentenceTransformers).
3.  **Storage**: Save vectors in a Vector Database (Pinecone, Chroma).
4.  **Retrieval**: When a user asks a question, convert it to a vector and find the most similar chunks in the DB.
5.  **Generation**: Feed the chunks + the question to the LLM.

## The Prompt

```text
You are a helpful assistant. Answer the user question based ONLY on the context provided below.

Context:
{retrieved_chunks}

Question:
{user_question}
```

See `code/simple_rag.py`.
