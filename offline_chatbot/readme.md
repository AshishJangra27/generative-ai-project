# Local LLM Chatbot

A simple **local AI chatbot** built using **Ollama, Llama 3.2, and Streamlit**.  
It provides a chat interface and stores conversations locally using JSON.

---

## Features

- Local LLM using Ollama  
- Llama 3.2 model support  
- Streamlit chat interface  
- Multiple chat sessions  
- Persistent chat history  

---

## Project Structure

```
local_llm_chatbot/
├── v0.py        # Basic Ollama test
├── v1.py        # Simple Streamlit chatbot
├── v2.py        # Chatbot with chat history
├── chats.json   # Stored conversations
└── README.md
```

---

## Installation

1. Create virtual environment

```
python3.11 -m venv venv
```

2. Activate environment

```
source venv/bin/activate
```

3. Install dependencies

```
pip install ollama streamlit
```

---

## Setup Ollama

Start Ollama server:

```
ollama serve
```

Download model:

```
ollama pull llama3.2
```

---

## Run Application

Start the chatbot:

```
streamlit run v2.py
```

Open in browser:

```
http://localhost:8501
```

---

## How It Works

1. User sends a message  
2. Message is sent to Ollama  
3. Llama 3.2 generates a response  
4. Chat history is saved in `chats.json`  

---

## License

MIT License
