# Generative AI Project Suite

A collection of four powerful AI-powered search and retrieval systems, each demonstrating different approaches to intelligent information retrieval, data querying, and question answering.



## Projects

### 1. **LLM Web Search** `/llm_web_search/`
Real-time web search with AI-powered answers using live content from the internet.

**Features:**
- Web search via Google Serper API
- Content scraping and cleaning
- AI answers using Google Gemini
- Streamlit web interface

**Tech Stack:** `Serper API` • `Gemini` • `Streamlit` • `BeautifulSoup`

---

### 2. **RAG-based Article Search** `/rag_based_article_search/`
Semantic search over 49K+ technical articles using vector embeddings and Pinecone.



**Features:**
- Vector similarity search
- Pinecone vector database
- Transformer-based embeddings
- Context-aware AI responses

**Tech Stack:** `Pinecone` • `Gemini` • `SentenceTransformers` • `HuggingFace`

---

### 3. **Advanced RAG Article Search** `/advanced_rag_based_article_search/`
Enhanced RAG pipeline with intelligent chunking and ChromaDB for local vector storage.

**Features:**
- Smart text chunking with LlamaIndex
- ChromaDB for persistent vector storage
- 100K+ searchable chunks
- Optimized retrieval pipeline

**Tech Stack:** `LlamaIndex` • `ChromaDB` • `Gemini` • `SentenceTransformers`

---

### 4. **Text-to-SQL via Prompt Engineering** `/text_to_sql_prompt_engineering/`
A natural language interface for relational databases that translates plain English into precise SQL queries.



**Features:**
- Natural language understanding for data queries
- Automatic schema context injection for accurate results
- Support for complex multi-table JOINs and filtering
- Conversational data insights generated from query results

**Tech Stack:** `Gemini` • `SQLite` • `SQL` • `Prompt Engineering`

---

## Use Cases

- **Internal Data Bots** for querying company databases without SQL knowledge
- **Knowledge Assistants** for enterprise documentation and wikis
- **Educational Tools** for technical content search and SQL learning
- **Research Helpers** for real-time information gathering from the web

## 🛠️ Quick Start

Each project includes detailed setup instructions in their respective folders. To get started, you will generally need to:
1. Obtain a Google AI Studio API key for Gemini.
2. Set up relevant environment variables for database connections (Pinecone, Serper, etc.).
3. Run the provided Jupyter notebooks or Streamlit applications.

## 👤 Author

Created by [Ashish Jangra](https://github.com/AshishJangra27)
