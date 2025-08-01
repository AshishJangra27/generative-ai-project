# AI-Powered Article Search with ChromaDB + Gemini

This project demonstrates a lightweight **RAG (Retrieval-Augmented Generation)** pipeline using:

- **Chunking**: Split articles into searchable pieces  
- **LlamaIndex**: Smart chunking and preprocessing  
- **ChromaDB**: Fast vector storage and semantic search  
- **Gemini 1.5 Flash**: Accurate answers using retrieved context  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aA6syFDGM_ME7hStWoQRb2VtgkugkJmU?usp=sharing)

---

## 🔄 Workflow

1. **Data Chunking**
   - Split full-length articles into ~100,000 chunks using LlamaIndex

2. **Embedding + Indexing**
   - Convert chunks into vectors using `all-MiniLM-L6-v2`  
   - Store in persistent ChromaDB

3. **Semantic Search**
   - Convert query to vector  
   - Retrieve top-k relevant chunks

4. **Answer Generation**
   - Combine context from results  
   - Ask Gemini 1.5 Flash for an answer

---

## 🧠 What This Project Can Do

- Process and chunk 49k+ articles into 100,000+ semantic units  
- Embed and index text into Chroma for fast search  
- Perform RAG-based Q&A using Gemini with precise retrieval  
- Easily adaptable to your own corpus  

---

## 📁 Dataset Info

- **Rows**: 49,328 articles  
- **Chunks**: 100,000+ after processing  
- **Fields**:
  - `title`: Article title  
  - `article`: Article content  

---

## 🚀 Getting Started

### 1. Clone Dataset and Install Dependencies
'''python
!git clone https://github.com/AshishJangra27/datasets/
!pip install llama-index
!pip install chromadb
'''

### 2. Preprocess and Chunk Articles
- Clean and normalize content  
- Chunk articles using LlamaIndex with overlap  

### 3. Generate Embeddings and Store in ChromaDB
- Use `SentenceTransformer("all-MiniLM-L6-v2")`  
- Persist vectors to local or remote Chroma index  

### 4. Search and Answer Queries
- Use vector similarity to get top-k matches  
- Pass the chunks as context to Gemini  
- Generate response  

---

## 💬 Example Usage

'''python
query = "What is a transformer model?"
response = answer_with_gemini(query)
print(response.text)
'''

---

## 📦 Output Files

- `data.csv`: Raw dataset  
- `articles.json`: Cleaned articles  
- `chunks.json`: Chunked articles  
- `chroma_index`: Stored vectors in Chroma  
- `query_logs.json`: Query and usage trace  

---

## 💡 Use Cases

- Search assistants for blogs, tutorials  
- Internal Q&A for enterprise docs  
- GenAI prototypes for educational content  
- Developer tools and codebase indexing  

---

## ✅ Final Notes

This notebook offers an end-to-end RAG pipeline:
- 100K+ chunks, fast retrieval, real-time LLM answers  
- Easily plug in your own documents  
- Extend to production or API-based deployment  

---

## 👤 Author

Made with ❤️ by [Ashish Jangra](https://github.com/AshishJangra27)  
Tech Stack: LlamaIndex · ChromaDB · Gemini · HuggingFace
