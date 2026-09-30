"""Unit tests for basic_agent tools."""
import unittest
from basic_agent.tools import get_current_time, calculate_expression, get_system_info


class TestAgentTools(unittest.TestCase):
    def test_get_current_time(self):
        result = get_current_time("UTC")
        self.assertIn("Current date and time", result)
        self.assertIn("UTC", result)

    def test_calculate_expression_valid(self):
        result = calculate_expression("12 * 8")
        self.assertEqual(result, "Result: 96")

        result2 = calculate_expression("(10 + 5) / 3")
        self.assertEqual(result2, "Result: 5.0")

    def test_calculate_expression_invalid_chars(self):
        result = calculate_expression("__import__('os').system('ls')")
        self.assertTrue(result.startswith("Error"))

    def test_get_system_info(self):
        result = get_system_info()
        self.assertIn("Operating System:", result)
        self.assertIn("Architecture:", result)


if __name__ == "__main__":
    unittest.main()
