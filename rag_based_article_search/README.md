# RAG-based Article Search Engine

This project walks you through building a smart article search engine that can **understand your question**, **search thousands of technical articles**, and give you a relevant, natural-language answer using **Google Gemini**.

## 🔗 Run in Google Colab

You can try this project directly in Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1p1nZFV0NI9rSIkmD_p3lDFeNvf_tFtYo?usp=sharing)


It uses the power of **Retrieval-Augmented Generation (RAG)** by combining:
- **Semantic search** (using embeddings + Pinecone)
- **LLM-based answering** (via Gemini with real context)

---

## 📌 What This Project Can Do

- Search across 49,000+ articles using vector similarity  
- Understand and embed article content using transformer models  
- Store and retrieve data efficiently using Pinecone  
- Answer questions with Gemini based on top-matching articles  
- Adapt easily to other datasets or domains  

---

## 📁 About the Dataset

- **Size**: 49,328 rows  
- **Columns**:
  - `title`: Title of the article  
  - `article`: The full content of the article  

---

## 🛠️ Getting Started

### Step 1: Clone the dataset
```
!git clone https://github.com/AshishJangra27/datasets/
```

### Step 2: Install the required packages
```
!pip install pinecone google-generativeai transformers
```

---

## 🚀 How It Works

### 1. Data Preparation
- Combine all article CSVs  
- Convert them to a clean JSON file: `articles.json`  

### 2. Generate Embeddings
- Use either:
  - `all-MiniLM-L6-v2` (lightweight transformer)
  - `Qwen3-Embedding-0.6B` (powerful multilingual model)
- Save outputs to `article_embeddings.json`

### 3. Store in Pinecone
- Connect to Pinecone with your API key  
- Create a `vector-db` index with cosine similarity  
- Upload article embeddings in batches  

### 4. Search & Retrieve
- Convert your query to an embedding  
- Use Pinecone to find top matching articles  
- Grab their content as context  

### 5. Ask Gemini
- Feed the context and your question to Gemini  
- Get a direct, LLM-generated answer  
- See token usage for transparency  

---

## 💬 Quick Example

```
query = "What is GAN?"
response = answer_with_gemini(query)
print(response.text)
```

---

## 📂 Output Files

- `data.csv`: Combined article data  
- `articles.json`: Clean article content  
- `article_embeddings.json`: Vector representations  
- `article_embeddings_qwen.json`: Alternative Qwen embeddings  

---

## 💡 Use It For

- AI-powered knowledge assistants  
- Educational bots for coding content  
- Internal document search  
- Prototyping GenAI search tools  

---

## ✅ Final Thoughts

You now have a full GenAI-powered system:  
A smart search engine that retrieves and explains article content like a human.

With just a few changes, you can plug in your own dataset, scale it, or build an app on top of it.

---

## 👤 Credits

Made with ❤️ by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by: Pinecone, Google Gemini, HuggingFace Transformers
