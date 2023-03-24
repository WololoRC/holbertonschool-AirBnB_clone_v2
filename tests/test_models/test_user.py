#!/usr/bin/python3
""" """
import unittest
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
        new_name = self.value()
        self.assertEqual(type(new_name.first_name), str)

    def test_last_name(self):
        """ """
        new_last = self.value()
        self.assertEqual(type(new_last.last_name), str)

    def test_email(self):
        """ """
        new_email = self.value()
        self.assertEqual(type(new_email.email), str)

    def test_password(self):
        """ """
        new_pass = self.value()
        self.assertEqual(type(new_pass.password), str)

if __name__ == '__main__':
    unittest.main()
