# Project Setup Guide

## 1. Create a Virtual Environment
```bash
python3.11 -m venv venv
```

## 2. Activate the Virtual Environment
```bash
source venv/bin/activate
```

## 3. Install Important Libraries
```bash
pip install ollama langchain streamlit langchain-community langchain-ollama langchain_google_genai
```

## 4. Download and Manage Llama 3.2 with Ollama

### Start Ollama Server
```bash
ollama serve
```

### Check Installed Models
```bash
ollama list
```

### Download Llama 3.2
```bash
ollama pull llama3.2
```

### Run Llama 3.2
```bash
ollama run llama3.2
```

### Stop the Model
```bash
ollama stop llama3.2
```

### Remove the Model
```bash
ollama rm llama3.2
```
