# 📊 Equity Research Analyst LLM Tool

A RAG application that facilitates the day-to-day work of financial analyst. It allows users to analyze multiple financial articles by asking natural language questions grounded in the source content.

![Final Look](finallook.png)

## 🚀 Key Features
- Paste **1–3 article URLs** for analysis
- Automatically:
    - Load and parse web content
    - Split text into chunks
    - Generate embeddings using OpenAI
    - Store vectors in a FAISS index
- Ask questions grounded in the indexed articles
- Answers are generated using retrieved context (RAG)

## 🧠 Architecture Overview
User \
↓
Streamlit UI \
↓ (HTTP requests)
FastAPI Backend \
├── URL Loader \
├── Text Splitter \
├── Embedding Model \
├── FAISS Vector Store \
└── LLM (OpenAI)

## 🛠 Tech Stack
### Frontend
- **Streamlit**
### Backend
- **FastAPI** 
- **LangChain** – orchestration
- **OpenAI API** – embeddings + LLM
- **LangSmith** – tracing

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Navigate to the project repo:
```bash
cd equity_research_tool_project
```

### 3. Enter the virtual environment(recommended) and Install the required dependencies:
```bash
python -m venv .venv
venv\Scripts\activate.bat     
pip install -r requirements.txt
```

### 4. Set up your keys by creating a .env file in the project root:
```bash
OPENAI_API_KEY= your_key_here
LANGSMITH_API_KEY = your_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT= https://api.smith.langchain.com
LANGCHAIN_PROJECT=my-tracing-test
```

## Usage
### 1. Run the FastAPI backend by executing:
```bash
uvicorn backend.api:app --reload
```

### 2. Open another terminal and Run the Streamlit frontend by executing:
```bash
streamlit run .\frontend\streamlit_app.py        
```

### 3. The web app will open in your browser:
- On the left sidebar, you can input upto 3 articles' URLs directly.
- Click on "Process URLs" to build the vector index and wait. 
- Ask questions about the given articles on the right
- You can try my articles and questions: 
- Articles: https://www.moneycontrol.com/news/business/banks/hdfc-bank-re-appoints-sanmoy-chakrabarti-as-chief-risk-officer-11259771.html
- Question: Who is Chief Risk Officer (CRO) of HDFC Bank on August 25th?