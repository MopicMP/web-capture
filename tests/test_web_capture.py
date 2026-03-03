"""Tests for web-capture."""

import pytest
from web_capture import capture


class TestCapture:
    """Test suite for capture."""

    def test_basic(self):
        """Test basic usage."""
        result = capture("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            capture("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = capture(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
