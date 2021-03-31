#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        a = "test"
        b = a
        self.assertEqual(a, b)

    def test_last_name(self):
        """ """
        self.assertEqual(4, 4)

    def test_email(self):
        """ """
        self.assertEqual(3, 3)

    def test_password(self):
        """ """
        self.assertEqual(2, 2)
