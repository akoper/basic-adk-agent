# Basic Google ADK Agent

A starter project showcasing a basic AI agent built using Google's **Agent Development Kit (ADK)** and Google Gemini models.

---

## Project Structure

```
basic-adk-agent/
├── .gitignore             # Git ignore file for Python, env, secrets, and IDEs
├── .env.example           # Example environment variables template
├── requirements.txt       # Project dependencies (google-adk, google-genai, etc.)
├── main.py                # Runner / entry point script
├── basic_agent/
│   ├── __init__.py        # Package exports (root_agent)
│   ├── agent.py           # Core agent definition with ADK
│   └── tools.py           # Custom Python functions/tools (time, calculator, system info)
└── README.md              # Project documentation
```

---

## Prerequisites

- **Python 3.10+**
- A **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## Quickstart Setup

### 1. Create and activate a virtual environment

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux / macOS
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Credentials

Copy `.env.example` to `.env` and insert your Gemini API key:

```bash
# Windows
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

Edit `.env`:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## Running the Agent

### Option A: Using Google ADK Dev UI (Web Interface)

Google ADK provides a built-in development UI to interact with, inspect, and evaluate agents:

```bash
adk web basic_agent
```

### Option B: Using Google ADK CLI

Run an interactive terminal session with the agent:

```bash
adk run basic_agent
```

### Option C: Python entry point

```bash
python main.py
```

---

## Agent Capabilities & Custom Tools

The agent is configured in `basic_agent/agent.py` and includes custom tools defined in `basic_agent/tools.py`:
- `get_current_time`: Returns current timestamp for time queries.
- `calculate_expression`: Evaluates arithmetic math operations.
- `get_system_info`: Returns host platform/OS details.
