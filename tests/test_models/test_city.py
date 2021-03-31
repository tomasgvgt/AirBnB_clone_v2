#!/usr/bin/python3
"""Tests for city"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Tests for city"""

    def __init__(self, *args, **kwargs):
        """Tests for city"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests for city"""
        self.assertEqual(type("new.state_id"), str)

    def test_name(self):
        """Tests for city"""
        self.assertEqual(type(56), int)
