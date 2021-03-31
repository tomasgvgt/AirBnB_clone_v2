#!/usr/bin/python3
"""unitary test for console Class"""

import unittest
import pep8


class ConsoleTests(unittest.TestCase):
    """Tests for Base class"""

    def test_try(self):
        """Test for module docstring"""
        self.assertTrue(2 > 1)




if __name__ == "__main__":
    unittest.main()