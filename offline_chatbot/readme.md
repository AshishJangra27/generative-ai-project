1. create a venv
python3.11 -m venv venv

2. activate venv
source venv/bin/activate

3. install important libraries
pip install ollama langchain streamlit langchain-community langchain-ollama langchain_google_genai

4. download llama3.2
ollama serve
ollama list
ollama pull llama3.2
ollama run llama3.2
ollama stop llama3.2
ollama rm llama3.2
