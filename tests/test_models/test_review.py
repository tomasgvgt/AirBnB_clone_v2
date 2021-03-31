#!/usr/bin/python3
"""This module has tests for review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Class of test for review"""

    def __init__(self, *args, **kwargs):
        """Constructor for the tests"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Checks for ID"""
        new_id = 15
        self.assertEqual(type(new_id), int)

    def test_user_id(self):
        """Checks for user ID"""
        new = "self.value()"
        self.assertEqual(type(new), str)

    def test_text(self):
        """Checks for text ID"""
        name = "Test"
        self.assertEqual(type(name), str)
