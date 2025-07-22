# RAG-based Article Search Engine

This project demonstrates how to build a smart, AI-powered article search system using a **Retrieval-Augmented Generation (RAG)** pipeline. It combines **semantic search** (via vector embeddings and Pinecone) with **contextual question answering** powered by **Google Gemini**.

---

## 📌 Project Highlights

- 🔍 Perform semantic search over 49,000+ GeeksforGeeks articles  
- 🧠 Generate high-quality embeddings using Transformer or Qwen models  
- 🗃️ Store and query vectors using Pinecone  
- 💬 Answer questions in natural language using Gemini LLM  
- 💡 Easily extendable to other domains and datasets  

---

## 📁 Dataset Overview

- **Source**: Technical articles from GeeksforGeeks  
- **Total Records**: 49,328  
- **Columns**:
  - `title`: The topic of the article  
  - `article`: Full article content  

---

## 🛠️ Setup Instructions

### 1. Clone the Dataset
```bash
!git clone https://github.com/AshishJangra27/datasets/
```

### 2. Install Dependencies
```bash
!pip install pinecone google-generativeai transformers
```

---

## 🚀 Workflow

### 1. **Data Preparation**
- Load and merge all article CSVs
- Convert the data into a single `articles.json` file

### 2. **Embedding Generation**
- Use either:
  - `all-MiniLM-L6-v2` from Sentence Transformers
  - `Qwen3-Embedding-0.6B` from Qwen
- Convert each article into a dense vector and save to `article_embeddings.json`

### 3. **Pinecone Vector Index**
- Initialize Pinecone client with API key  
- Create a `vector-db` index (dimension: 384, metric: cosine)  
- Batch upload vectors with truncated article metadata

### 4. **Semantic Search**
- Embed the user’s query using the same model
- Search for top-k similar articles in Pinecone
- Retrieve their metadata (article text)

### 5. **Gemini Answering**
- Pass the retrieved content + question to Gemini
- Use `gemini-1.5-flash` to generate an answer based on context
- Display the answer and token usage

---

## 💬 Example

```python
q = "What is GAN?"
response = answer_with_gemini(q)
print(response.text)
```

---

## 📦 Output Files

- `data.csv`: Merged article data  
- `articles.json`: JSON-formatted article content  
- `article_embeddings.json`: Embeddings with metadata  
- `article_embeddings_qwen.json`: Optional Qwen-based embeddings  

---

## 📈 Use Cases

- Build internal knowledge assistants  
- Develop educational bots  
- Create GenAI-based document search engines  
- Extend for multilingual or domain-specific content

---

## ✅ Conclusion

This notebook provides a complete, working example of how to combine semantic search with large language models. With minimal customization, it can be scaled into a production-ready assistant or integrated into web applications.

---

## 📌 Credits

Built by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by: Pinecone, Google Gemini, HuggingFace Transformers
