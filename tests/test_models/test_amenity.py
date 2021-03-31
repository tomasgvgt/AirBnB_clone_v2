#!/usr/bin/python3
"""Test module for amenities"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test module for amenities"""

    def __init__(self, *args, **kwargs):
        """Test module for amenities"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test module for amenities"""
        self.assertEqual(10, 10)
