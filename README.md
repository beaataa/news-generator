# news-generator

# 📰 AI News Article Generator

An AI-powered application that automatically generates news articles based on user-selected topics. The app fetches real-time news data and uses AI to create comprehensive, well-structured articles.

## Features

- Real-time news data fetching using NewsAPI
- AI-powered article generation using LangChain and Llama3
- Content validation and quality checks
- User-friendly Streamlit interface
- Article download functionality
- Source article tracking and references
- Word count and validation metrics

## Prerequisites

Before running the application, make sure you have:

1. Ollama Installed and Model Downloaded
-   Install Ollama on your operating system: [https://ollama.com](https://ollama.com)
-   Download the required model (e.g., Llama3) by running:
```bash
ollama pull llama3
```
2. Python 3.8 or higher
3. A NewsAPI key (get one at [https://newsapi.org](https://newsapi.org))

## 📦 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd news-generator
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root directory:
```bash
NEWSAPI_KEY=your_api_key_here
```

## Project Structure

```
news-generator/
├── .env                 # Environment variables
├── news_app.py          # Streamlit web application
├── main.py              # Generate articles in terminal
├── requirements.txt     # Project dependencies
└── src/
    ├── __init__.py     # Package initializer
    ├── news_fetcher.py # News API integration
    ├── generator.py    # Article generation logic
    └── validator.py    # Content validation
```

## 🚀 Usage

1. Terminal execution:
-   To run the CLI-based news generator:
```bash
python main.py
```

2. Web application:
-   Start the Ollama Model Server. Open a new terminal and run:
```bash
ollama serve
```
-   Run the Streamlit App. In another terminal, run:
```bash
streamlit run news_app.py
```

-   Enter a topic in the text input field

-   Click "Generate Article" to create your news article

## Components

### NewsFetcher
- Handles integration with NewsAPI
- Fetches relevant news articles based on user topics
- Manages API requests and responses

### NewsGenerator
- Processes fetched news data
- Generates coherent articles using AI
- Implements LangChain and Llama3 for content generation

### NewsValidator
- Validates generated content
- Checks for speculative language
- Ensures article length requirements
- Performs quality control

## Dependencies

- `streamlit`: Web application framework
- `python-dotenv`: Environment variable management
- `requests`: HTTP requests for API calls
- `feedparser`: RSS feed parsing
- `langchain`: AI text generation
- `langchain_community`: Additional LangChain components
- `langchain_ollama`: Integration for Llama3

## Important Notes

- Keep your NewsAPI key confidential
- The free tier of NewsAPI has usage limits
- Generated articles should be reviewed for accuracy
- AI-generated content may require fact-checking

## Acknowledgments

- NewsAPI for providing news data
- Streamlit for the web framework
- LangChain community for tools and support in AI text generation
- Ollama for the local Llama model server integration
