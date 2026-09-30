"""Entry point to run the Google ADK Agent interactively or test execution."""
import os
import sys
from dotenv import load_dotenv

# Load environment configuration
load_dotenv()


def main():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Warning: Neither GEMINI_API_KEY nor GOOGLE_API_KEY is set.")
        print("Please set your Gemini API key in a .env file or environment variables.")
        print("See .env.example for details.\n")

    try:
        from basic_agent.agent import root_agent
    except Exception as e:
        print(f"Error importing agent: {e}")
        sys.exit(1)

    print("=" * 60)
    print(" Google ADK (Agent Development Kit) - Basic Agent")
    print("=" * 60)
    if root_agent:
        print(f"Agent Name : {getattr(root_agent, 'name', 'basic_assistant')}")
        print(f"Model      : {getattr(root_agent, 'model', 'gemini-2.5-flash')}")
        tools = getattr(root_agent, 'tools', [])
        print(f"Tools ({len(tools)}): {', '.join([t.__name__ if hasattr(t, '__name__') else str(t) for t in tools])}")
    print("-" * 60)
    print("You can interact with this agent via the ADK CLI / Web UI:")
    print("  adk web basic_agent")
    print("  or")
    print("  adk run basic_agent")
    print("=" * 60)


if __name__ == "__main__":
    main()
