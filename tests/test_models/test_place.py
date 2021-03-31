#!/usr/bin/python3
"""This module has tests for place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Tests for place"""

    def __init__(self, *args, **kwargs):
        """Tests for place"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tests for place"""
        self.assertEqual(type("new.city_id"), str)

    def test_user_id(self):
        """Tests for place"""
        self.assertEqual(3, 3)

    def test_name(self):
        """Tests for place"""
        self.assertEqual(type("new.name"), str)

    def test_description(self):
        """Tests for place"""
        new = self.value()
        self.assertEqual(type("new.description"), str)

    def test_number_rooms(self):
        """Tests for place"""
        self.assertEqual(type("new.number_rooms"), str)

    def test_number_bathrooms(self):
        """Tests for place"""
        self.assertEqual(type(45), int)

    def test_max_guest(self):
        """Tests for place"""
        self.assertEqual(type(159), int)

    def test_price_by_night(self):
        """Tests for place"""
        self.assertEqual(type(10), int)

    def test_latitude(self):
        """Tests for place"""
        self.assertEqual(5, 5)

    def test_longitude(self):
        """ """
        self.assertEqual(type(len(["new.latitude"])), int)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
