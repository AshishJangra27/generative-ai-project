# Sapiens Q&A Bot (BM25 + Gemma LLM)

This project demonstrates how to build a **document-based Question Answering system** using the book *Sapiens: A Brief History of Humankind* as the knowledge source. It combines **BM25 retrieval** with a **Gemma LLM** to generate answers strictly from the book’s content.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1N_HwAMbuVG9iGaekfnG04MiAEJwfS4-C?usp=sharing)

By integrating **classical information retrieval (BM25)** with **LLM-based reasoning**, this project shows how to build an efficient and grounded Q&A system without vector databases.

---

## What This Project Covers

- **PDF Knowledge Ingestion**: Extracting and processing text from a book  
- **Text Chunking**: Splitting large documents into manageable chunks  
- **BM25 Retrieval**: Ranking relevant chunks based on query similarity  
- **Context-Based Answering**: Generating answers using only retrieved content  
- **Efficient Pipeline**: Combining lightweight retrieval with LLM  

---

## Tech Stack Used

- **LLM**: Google Gemma (gemma-4-E2B-it)  
- **Retriever**: BM25Okapi (rank_bm25)  
- **PDF Processing**: pypdf  
- **Framework**: Hugging Face Transformers  
- **Language**: Python  
- **Environment**: Google Colab  

---

## Project Workflow

### 1. PDF Processing
The book is loaded and text is extracted from all pages.

### 2. Text Chunking
The extracted text is divided into smaller chunks for efficient retrieval.

### 3. Tokenization
Each chunk is tokenized to prepare for BM25 retrieval.

### 4. Retriever Initialization
A BM25Okapi retriever is created using the tokenized corpus.

### 5. Query Processing
The user query is tokenized and matched against document chunks.

### 6. Context Retrieval
Top relevant chunks are selected as context.

### 7. Answer Generation
The context and query are passed to the Gemma model to generate an answer.

---

## Key Features

- **No Vector Database Required**  
- **Grounded Responses** from book content only  
- **Efficient Retrieval** using BM25  
- **Reusable Pipeline** for any PDF-based dataset  

---

## Learning Outcome

By completing this project, you will understand:

- How document-based Q&A systems work  
- Difference between BM25 and embedding-based retrieval  
- How to process PDFs for AI applications  
- How to combine retrieval with LLMs  
- How to build lightweight RAG systems  

This forms the foundation for building:

- Document search engines  
- AI study assistants  
- Knowledge-based chatbots  
- Research assistants  

---

## Credits

Made by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by Hugging Face Transformers and Google Gemma  
