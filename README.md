# LangGraph Interactive Chatbot Suite

An end-to-end, modular collection of AI Chatbot implementations built using **LangGraph**, **LangChain**, **OpenAI**, and **Streamlit**. 

This suite demonstrates progressive chatbot capabilities ranging from basic conversational nodes and persistent SQLite checkpointers to custom tool execution, PDF Retrieval-Augmented Generation (RAG) with FAISS vector stores, and Model Context Protocol (MCP) server integration.

---

## 🌟 Key Features

1. **Basic Chatbot (`langgraph_backend.py` + `streamlit_frontend.py`)**
   - Simple LangGraph state graph using `InMemorySaver` checkpointer.
   - Ideal for light, single-session conversational workflows.

2. **Database-Backed Chatbot (`langgraph_database_backend.py` + `streamlit_frontend_database.py`)**
   - Persistent thread management backed by `SqliteSaver` (`chatbot.db`).
   - Retains conversation history across user sessions with sidebar thread switching.

3. **Tool-Calling Chatbot (`langgraph_tool_backend.py` + `streamlit_frontend_tool.py`)**
   - Autonomous tool selection and execution using LangGraph prebuilt `ToolNode` and `tools_condition`.
   - Built-in tools:
     - 🧮 **Calculator**: Basic arithmetic (`add`, `sub`, `mul`, `div`).
     - 📈 **Stock Price**: Live market quotes via Alpha Vantage API.
     - 🔍 **Web Search**: Real-time web queries via DuckDuckGo Search.

4. **RAG PDF Chatbot (`langgraph_rag_backend.py` + `streamlit_rag_frontend.py`)**
   - Thread-isolated PDF document ingestion and retrieval.
   - Text chunking via `RecursiveCharacterTextSplitter` and in-memory `FAISS` vector index using `OpenAIEmbeddings`.
   - Combined system prompting allowing the assistant to seamlessly switch between document Q&A, stock lookup, calculations, and web search.

5. **Model Context Protocol (MCP) Chatbot (`langgraph_mcp_backend.py` + `streamlit_frontend_mcp.py`)**
   - Asynchronous checkpointer (`AsyncSqliteSaver`) with `MultiServerMCPClient` support.
   - Extensible for connecting to stdio and HTTP-based MCP servers.

6. **Streaming UI (`streamlit_frontend_streaming.py`, `streamlit_frontend_threading.py`)**
   - Real-time token streaming using Streamlit's `st.write_stream` and LangGraph event streaming.

---

## 🛠️ Technology Stack

- **Frameworks**: [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), [Streamlit](https://streamlit.io/)
- **LLM & Embeddings**: OpenAI (`gpt-4o-mini`, `text-embedding-3-small`)
- **Vector Search & Document Processing**: FAISS (`faiss-cpu`), PyPDF (`pypdf`)
- **Database & Persistence**: SQLite (`sqlite3`, `aiosqlite`, `langgraph-checkpoint-sqlite`)
- **Tools & Utilities**: DuckDuckGo Search, Alpha Vantage API, `python-dotenv`, `pytest`

---

## 📁 Directory Structure

```text
chatbot-in-langgraph/
├── langgraph_backend.py             # Basic backend graph with in-memory checkpointer
├── langgraph_database_backend.py    # Database backend with SQLite checkpointer & thread management
├── langgraph_tool_backend.py        # Tool-enabled backend (Calculator, Stock Price, Web Search)
├── langgraph_rag_backend.py         # RAG PDF ingestion & FAISS retriever backend
├── langgraph_mcp_backend.py         # Async MCP-enabled backend (MultiServerMCPClient)
├── streamlit_frontend.py            # Streamlit UI for Basic Chatbot
├── streamlit_frontend_database.py   # Streamlit UI for Persistent Database Chatbot
├── streamlit_frontend_streaming.py  # Streamlit UI demonstration for message streaming
├── streamlit_frontend_threading.py  # Streamlit UI demonstration for multi-threaded conversations
├── streamlit_frontend_tool.py       # Streamlit UI for Tool-Calling Chatbot
├── streamlit_frontend_mcp.py        # Streamlit UI for MCP Chatbot
├── streamlit_rag_frontend.py        # Streamlit UI for PDF Document RAG Chatbot
├── test_backends.py                 # Automated unit tests for all backend graphs & tools
├── requirements.txt                 # Project Python dependencies
├── .env.example                     # Environment configuration template
└── .gitignore                    # Git ignore file for secrets, DBs, and virtualenvs
```

---

## 📋 Prerequisites

- **Python 3.10+** installed on your system.
- An **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys)).
- An **Alpha Vantage API Key** (Optional for stock price tool, [Get a free key here](https://www.alphavantage.co/support/#api-key)).

---

## ⚙️ Installation & Setup

1. **Clone or navigate to the repository directory**:
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd chatbot-in-langgraph
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On macOS/Linux:
   python3 -m venv .venv
   source .venv/bin/activate

   # On Windows (PowerShell):
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Copy `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```
   Open `.env` in a text editor:
   ```env
   OPENAI_API_KEY=sk-proj-...
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
   ```

---

## 🚀 Running the Streamlit Applications

You can run any of the Streamlit frontend interfaces depending on the desired feature set:

### 1. Run the RAG PDF Chatbot (Recommended)
```bash
streamlit run streamlit_rag_frontend.py
```
*Upload a PDF in the sidebar and ask questions about the document, or ask for stock prices, calculations, and general search queries!*

### 2. Run the Tool-Calling Chatbot
```bash
streamlit run streamlit_frontend_tool.py
```

### 3. Run the Persistent Database Chatbot
```bash
streamlit run streamlit_frontend_database.py
```

### 4. Run the Basic Chatbot
```bash
streamlit run streamlit_frontend.py
```

### 5. Run the MCP Chatbot
```bash
streamlit run streamlit_frontend_mcp.py
```

---

## 🧪 Running Automated Tests

Run the backend test suite using `pytest`:

```bash
pytest test_backends.py
```

To verify Python syntax across all modules:

```bash
python -m py_compile *.py
```

---
