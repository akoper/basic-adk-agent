"""Basic Agent definition using Google ADK."""
from __future__ import annotations
import os
from dotenv import load_dotenv

# Load environment variables from .env file if available
load_dotenv()

# Import Agent from Google ADK
try:
    from google.adk.agents import Agent
except ImportError:
    # Fallback import style if package structure differs
    try:
        from google.adk import Agent
    except ImportError:
        Agent = None  # Handled when dependencies are installed

from .tools import get_current_time, calculate_expression, get_system_info

# Model selection - defaults to Gemini 2.5 Flash / 2.0 Flash
MODEL_NAME = os.getenv("ADK_MODEL_NAME", "gemini-3.8-flash")

# Define the root agent
if Agent is not None:
    root_agent = Agent(
        name="basic_assistant",
        model=MODEL_NAME,
        description="A friendly, general-purpose AI assistant powered by Google ADK and Gemini.",
        instruction=(
            "You are a helpful, clear, and concise AI assistant built with Google Agent Development Kit (ADK). "
            "You have access to tools for checking the current time, calculating mathematical expressions, "
            "and retrieving system information. Use tools whenever requested or needed to answer accurately."
        ),
        tools=[get_current_time, calculate_expression, get_system_info],
    )
else:
    root_agent = None
