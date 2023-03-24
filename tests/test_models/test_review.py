#!/usr/bin/python3
""" """
import unittest
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
        new = self.value()
        self.assertNotEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.text), str)

if __name__ == '__main__':
    unittest.main()
