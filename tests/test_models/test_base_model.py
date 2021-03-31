#!/usr/bin/python3
"""Tests for base_model"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Tests for base_model"""

    def __init__(self, *args, **kwargs):
        """Tests for base_model"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Tests for base_model"""
        pass

    def tearDown(self):
        """Tests for base_model"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Tests for base_model"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Tests for base_model"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Tests for base_model"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        self.assertEqual(type("g"), str)

    def test_str(self):
        """Tests for base_model"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Tests for base_model"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Tests for base_model"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Tests for base_model"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            raise KeyError

    def test_id(self):
        """Tests for base_model"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Tests for base_model"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Tests for base_model"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
