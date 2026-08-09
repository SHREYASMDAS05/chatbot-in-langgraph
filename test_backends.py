import os
import unittest
import langgraph_backend
import langgraph_database_backend
import langgraph_tool_backend
import langgraph_rag_backend
import langgraph_mcp_backend


class TestLangGraphBackends(unittest.TestCase):

    def test_basic_backend_compiled(self):
        """Test basic backend graph object initialization."""
        self.assertIsNotNone(langgraph_backend.chatbot)

    def test_database_backend_compiled(self):
        """Test database backend graph object initialization and thread retrieval."""
        self.assertIsNotNone(langgraph_database_backend.chatbot)
        threads = langgraph_database_backend.retrieve_all_threads()
        self.assertIsInstance(threads, list)

    def test_tool_backend_compiled_and_calculator(self):
        """Test tool backend graph and calculator tool execution."""
        self.assertIsNotNone(langgraph_tool_backend.chatbot)

        # Test calculator tool math logic
        calc_result = langgraph_tool_backend.calculator.invoke(
            {"first_num": 10, "second_num": 5, "operation": "add"}
        )
        self.assertEqual(calc_result.get("result"), 15)

        div_zero = langgraph_tool_backend.calculator.invoke(
            {"first_num": 10, "second_num": 0, "operation": "div"}
        )
        self.assertIn("error", div_zero)

    def test_stock_price_tool_missing_key(self):
        """Test stock price tool when ALPHA_VANTAGE_API_KEY is not set."""
        # Ensure env var is unset during test
        orig_key = os.environ.pop("ALPHA_VANTAGE_API_KEY", None)
        try:
            res = langgraph_tool_backend.get_stock_price.invoke({"symbol": "AAPL"})
            self.assertIn("error", res)
        finally:
            if orig_key:
                os.environ["ALPHA_VANTAGE_API_KEY"] = orig_key

    def test_rag_backend_compiled(self):
        """Test RAG backend graph compilation and helper functions."""
        self.assertIsNotNone(langgraph_rag_backend.chatbot)
        threads = langgraph_rag_backend.retrieve_all_threads()
        self.assertIsInstance(threads, list)
        self.assertFalse(langgraph_rag_backend.thread_has_document("test-thread-123"))

    def test_mcp_backend_compiled(self):
        """Test MCP backend graph initialization."""
        self.assertIsNotNone(langgraph_mcp_backend.chatbot)
        threads = langgraph_mcp_backend.retrieve_all_threads()
        self.assertIsInstance(threads, list)


if __name__ == "__main__":
    unittest.main()
