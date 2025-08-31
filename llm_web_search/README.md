# LLM Web Search

A Python application that searches the web, scrapes content from relevant sources, and generates AI-powered answers using the collected data.

---

## Features

- Web search using Google Serper API  
- Content scraping and cleaning from multiple websites  
- AI-powered answers using Google Gemini  
- Simple Streamlit-based web interface  
- Token usage tracking for transparency  
- Organized logging with timestamped folders  

---

## Project Structure

```
llm_web_search/
├── client.py          # Streamlit interface
├── main.py            # Command-line interface
├── get_links.py       # Web search functionality
├── scrape.py          # Scraping logic
├── cleaning.py        # Content processing
├── llm.py             # AI model integration
├── requirements.txt   # Project dependencies
├── .env               # Environment variables
└── logs/              # Saved content
```

---

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/AshishJangra27/generative-ai-project
   cd generative-ai-project/llm_web_search
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up API keys by creating a `.env` file:
   ```
   SERPER_API_KEY=your_serper_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

---

## Required API Keys

- [Serper.dev](https://serper.dev) – for web search  
- [Google AI Studio](https://makersuite.google.com/app/apikey) – for Gemini AI  

---

## Usage

### Web Interface (Recommended)
```
streamlit run client.py
```
Open your browser and go to: `http://localhost:8501`

### Command Line
Edit the `topic` variable in `main.py` and run:
```
python main.py
```

---

## How It Works

1. Searches the web for relevant links  
2. Scrapes content from selected websites  
3. Processes and merges the collected text  
4. Uses Gemini AI to generate an answer  
5. Displays the response and token usage  

---

## Dependencies

- `requests` – for web requests  
- `beautifulsoup4` – for HTML parsing  
- `python-dotenv` – for environment variable management  
- `google-generativeai` – for Gemini integration  
- `streamlit` – for the web interface  
- `numpy<2` – compatibility fix  

---

## Configuration

- Default model: `gemini-1.5-flash` (set in `llm.py`)  
- Request timeout: 10 seconds (`scrape.py`)  
- Logs: All scraped content stored in `logs/`  

---

## Notes

- The AI answers are based only on scraped web content  
- Training data is not used for responses  
- Websites are scraped respectfully, following `robots.txt` rules  
- All collected content is saved locally for review and debugging  

---

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

---

## License

This project is released under the MIT License.
