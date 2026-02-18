# LangGraph Agentic AI – Streamlit Application

An **Agentic AI application** built using **LangGraph, Streamlit, and Groq LLM**.
The project demonstrates how to build **tool-using AI agents**, structured workflows, and multi-usecase chatbot systems.

---

## 🚀 Features

* Agentic workflows using **LangGraph**
* Modular architecture
* Streamlit-based interactive UI
* Support for multiple use cases:

  * Basic Chatbot
  * Chatbot with Tools
  * AI News Summarizer
* External tool integration (Tavily Search API)
* Configurable LLM selection
* Structured graph execution and visualization

---

## 🧠 Architecture Overview

The system follows an **Agentic AI pipeline**:

User Input → Streamlit UI → Graph Builder → Agent → Tools → LLM → Response → UI

Core Components:

* **UI Layer**

  * Collects user input
  * Displays responses
* **LLM Layer**

  * Groq LLM integration
* **Graph Layer**

  * LangGraph workflows
* **Tools Layer**

  * Search tools
  * Retrieval tools
* **Output Layer**

  * Streamlit rendering

---

## 📂 Project Structure

```
ChatBot_with_Langgraph/
│
├── app.py
├── main.py
│
├── src/
│   ├── langgraphs_agentic_ai/
│   │   ├── graphs/
│   │   │   ├── graphs_builder.py
│   │   │
│   │   ├── llms/
│   │   │   ├── groqllm.py
│   │   │
│   │   ├── tools/
│   │   │   ├── search_tool.py
│   │   │
│   │   ├── ui/
│   │   │   ├── streamlit/
│   │   │   │   ├── load_ui.py
│   │   │   │   ├── display_result.py
│   │   │   │   └── config_ui.py
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/langgraph-agentic-ai.git
cd langgraph-agentic-ai
```

### 2. Create Virtual Environment (uv recommended)

```bash
uv venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧩 Supported Use Cases

### 1. Basic Chatbot

Simple conversational AI using Groq LLM.

Flow:

```
User → Agent → LLM → Response
```

---

### 2. Chatbot with Tools

Agent decides:

* Answer directly
* Call tool
* Return result

Flow:

```
User → Agent → Tool Decision → Tool → Agent → Response
```

---

### 3. AI News Summarizer

Uses:

* Tavily Search
* LLM summarization

Flow:

```
User Topic → Search Tool → Results → LLM Summary → Output
```

---

## 🔄 LangGraph Workflow

Typical graph structure:

```
START
  ↓
Agent Node
  ↓
Tool Node (if needed)
  ↓
Agent
  ↓
END
```

Agent decides dynamically whether to call tools.

---

## 🛠 Technologies Used

* LangGraph
* LangChain
* Streamlit
* Groq LLM
* Tavily Search API
* Python

---

## 📊 Graph Visualization

The application supports workflow visualization using Mermaid diagrams generated from LangGraph.

---

## 🧪 Example Questions

Basic Chat:

```
Explain agentic AI
```

Tool Use:

```
Latest AI news today
```

Summarization:

```
Summarize news about OpenAI
```

---

## 🧯 Common Issues

### Module Not Found

Install missing packages:

```bash
uv add package_name
```

---

### Session State Error

Initialize before use:

```python
if "IsFetchButtonClicked" not in st.session_state:
    st.session_state.IsFetchButtonClicked = False
```

---

### Tavily Deprecation Warning

Install updated package:

```bash
pip install -U langchain-tavily
```

---

## 📌 Future Improvements

* Memory support
* RAG integration
* Multi-agent workflows
* Pinecone or Chroma vector DB support
* Deployment on cloud

