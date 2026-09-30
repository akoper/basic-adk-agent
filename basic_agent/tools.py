"""Sample tools for the basic Google ADK agent."""
from datetime import datetime
import platform


def get_current_time(timezone_name: str = "UTC") -> str:
    """Returns the current date and time.

    Args:
        timezone_name: Name of the timezone (defaults to UTC/system time).
    """
    now = datetime.now()
    return f"Current date and time ({timezone_name}): {now.strftime('%Y-%m-%d %H:%M:%S')}"


def calculate_expression(expression: str) -> str:
    """Evaluates a safe mathematical expression.

    Args:
        expression: Mathematical expression to evaluate (e.g., '24 * 7' or '100 / 4').
    """
    allowed_chars = set("0123456789+-*/(). %")
    if not all(c in allowed_chars for c in expression):
        return "Error: Expression contains invalid characters."
    try:
        # Evaluate arithmetic expression safely with no globals or builtins
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"


def get_system_info() -> str:
    """Provides basic information about the operating system and platform."""
    return (
        f"Operating System: {platform.system()} {platform.release()} "
        f"({platform.version()}), Architecture: {platform.machine()}"
    )
