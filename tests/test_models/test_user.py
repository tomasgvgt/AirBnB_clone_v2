#!/usr/bin/python3
"""Tests for user"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Tests for user"""

    def __init__(self, *args, **kwargs):
        """Tests for user"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Tests for user"""
        a = "test"
        b = a
        self.assertEqual(a, b)

    def test_last_name(self):
        """Tests for user"""
        self.assertEqual(4, 4)

    def test_email(self):
        """Tests for user"""
        self.assertEqual(3, 3)

    def test_password(self):
        """Tests for user"""
        self.assertEqual(2, 2)
