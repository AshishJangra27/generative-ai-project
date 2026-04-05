# RAG-based Article Search Engine (Gemini & Qwen Embeddings)

This project demonstrates how to build a **Retrieval-Augmented Generation (RAG) system** using **Sentence Transformers** and the **Google Gemini API**. It showcases how to create a lightweight semantic search engine that retrieves relevant articles and generates accurate answers based strictly on context.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NJ67hZiQ5NLCFj78CrAiKNbCNvdRlvaf?usp=sharing)

By combining **vector search** with **LLM-based reasoning**, this project simulates how modern AI assistants retrieve and respond to user queries intelligently.

---

## What This Project Covers

- **Semantic Search**: Using transformer-based embeddings to understand meaning, not just keywords  
- **Embedding Generation**: Converting articles into dense vector representations  
- **Similarity Retrieval**: Finding relevant articles using cosine similarity  
- **Context-Based Answering**: Generating answers using Gemini strictly from retrieved data  
- **Lightweight RAG Pipeline**: No external vector database required  

---

## Tech Stack Used

- **LLM**: Google Gemini (gemini-2.5-flash)  
- **Embeddings**: Qwen3-Embedding-0.6B (Sentence Transformers)  
- **Computation**: NumPy  
- **Data Handling**: Pandas  
- **Language**: Python  
- **Environment**: Google Colab  

---

## Project Workflow

### 1. Data Loading
The dataset is loaded from CSV files containing article titles and content.

### 2. Embedding Generation
Each article is converted into a vector representation using a transformer-based embedding model.

### 3. Query Encoding
The user query is encoded into the same vector space as the articles.

### 4. Similarity Search
Cosine similarity is computed between the query and all article embeddings to retrieve the most relevant results.

### 5. Context Creation
Top-k matching articles are combined to form the context.

### 6. Answer Generation
The context and query are passed to Gemini, which generates a response strictly based on the retrieved information.

---

## Key Features

- **No Vector Database Required**: Uses NumPy for similarity search  
- **Context-Aware Answers**: Responses are grounded in retrieved articles  
- **Efficient Pipeline**: Simple and easy to implement  
- **Flexible Design**: Can be adapted to any dataset  

---

## Learning Outcome

By completing this project, you will understand:

- How Retrieval-Augmented Generation (RAG) works  
- How to generate and use embeddings for semantic search  
- How to implement cosine similarity for retrieval  
- How to integrate LLMs with external context  
- How to build a basic end-to-end GenAI pipeline  

This forms the foundation for building:

- AI-powered search engines  
- Knowledge-based chatbots  
- Document retrieval systems  
- Domain-specific assistants  

---

## Credits

Made by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by Sentence Transformers and Google Gemini API  
