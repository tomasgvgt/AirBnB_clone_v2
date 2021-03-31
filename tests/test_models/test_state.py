#!/usr/bin/python3
"""Tests for state"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Tests for state"""

    def __init__(self, *args, **kwargs):
        """Tests for state"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests for state"""
        name = "test_check"
        self.assertEqual(type(name), str)
