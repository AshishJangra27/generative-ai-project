# LLM Web Search

A Python application that searches the web for information on any topic, scrapes relevant content, and uses AI to provide accurate answers based on the gathered data.

## 🚀 Features

- **Web Search**: Automatically finds relevant links using Google Serper API
- **Content Scraping**: Extracts and cleans content from multiple web sources
- **AI-Powered Answers**: Uses Google Gemini AI to provide answers based on scraped content
- **Streamlit UI**: Clean, minimalistic web interface for easy interaction
- **Token Tracking**: Displays detailed token usage information for AI calls
- **Organized Logging**: Saves all scraped content in timestamped folders

## 📁 Project Structure

```
llm_web_search/
├── client.py          # Streamlit web interface
├── main.py           # Command-line interface
├── get_links.py      # Web search functionality
├── scrape.py         # Content scraping and extraction
├── cleaning.py       # Log file processing
├── llm.py            # AI integration (Google Gemini)
├── requirements.txt  # Python dependencies
├── .env             # Environment variables
└── logs/            # Scraped content storage
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd llm_web_search
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file with your API keys:
   ```env
   SERPER_API_KEY=your_serper_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 🔑 API Keys Required

- **Google Serper API**: Get your free API key at [serper.dev](https://serper.dev)
- **Google Gemini API**: Get your API key at [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🖥️ Usage

### Web Interface (Recommended)
```bash
python -m streamlit run client.py
```
Then open http://localhost:8501 in your browser.

### Command Line
Edit the `topic` variable in `main.py` and run:
```bash
python main.py
```

## 📋 How It Works

1. **Search**: Finds relevant web links for your topic using Google Serper API
2. **Scrape**: Extracts content from multiple websites using BeautifulSoup
3. **Process**: Combines all content into a comprehensive context
4. **Answer**: Uses Google Gemini AI to provide answers based only on the scraped content
5. **Display**: Shows the AI-generated answer with token usage statistics

## 📦 Dependencies

- `requests` - HTTP requests for web scraping
- `beautifulsoup4` - HTML parsing and content extraction
- `python-dotenv` - Environment variable management
- `google-generativeai` - Google Gemini AI integration
- `streamlit` - Web interface framework
- `numpy<2` - NumPy compatibility fix

## 🎯 Example Usage

**Topic**: "latest AI developments 2024"

**Process**:
1. Searches for recent AI news and articles
2. Scrapes content from 10+ relevant websites
3. Combines all information into a comprehensive context
4. AI analyzes the content and provides a detailed summary

**Output**: A well-researched answer based on current web content, not outdated training data.

## 🔧 Configuration

- **Model**: Uses `gemini-1.5-flash` by default (configurable in `llm.py`)
- **Timeout**: 10-second timeout for web requests (configurable in `scrape.py`)
- **Log Storage**: All scraped content saved in `logs/` directory with timestamps

## 📊 Token Usage

The application displays detailed token consumption:
- Input tokens (your prompt + context)
- Output tokens (AI response)
- Total tokens used
- Model information

## 🚨 Important Notes

- Answers are based **only** on scraped web content
- The AI is instructed not to use its training data
- Content is saved locally for transparency and debugging
- Respects website robots.txt and implements reasonable delays

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.
