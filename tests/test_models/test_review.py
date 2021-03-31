#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new_id = 15
        self.assertEqual(type(new_id), int)

    def test_user_id(self):
        """ """
        new = "self.value()"
        self.assertEqual(type(new), str)

    def test_text(self):
        """ """
        name = "Test"
        self.assertEqual(type(name), str)
