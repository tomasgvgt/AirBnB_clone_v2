#!/usr/bin/python3
"""This module has tests for console class"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
import io


class ConsoleTests(unittest.TestCase):
    """Tests for Base class"""

    def test_try(self):
        """Test for module docstring"""
        self.assertTrue(2 > 1)

    def test_create(self):
        """Test for create feature"""
        stdout = None
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="Antioquia"')
            stdout = f.getvalue()
            self.assertEqual(type(stdout), str)

if __name__ == "__main__":
    unittest.main()