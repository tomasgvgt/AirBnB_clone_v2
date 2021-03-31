#!/usr/bin/python3
"""This module has tests for console class"""
import unittest


class ConsoleTests(unittest.TestCase):
    """Tests for Base class"""

    def test_try(self):
        """Test for module docstring"""
        self.assertTrue(2 > 1)

if __name__ == "__main__":
    unittest.main()