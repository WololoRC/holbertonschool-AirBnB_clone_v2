#!/usr/bin/python3
""" base model, models """

import unittest
from console import HBNBCommand
from models.state import State


class test_DBstorage(unittest.TestCase):
    """ """
    def create(self):
        """some"""
        return HBNBCommand()

    def test_newState(self):
        """some"""
        new = State(name='California')
        self.assertEqual(new.name, 'California')


if __name__ == '__main__':
    unittest.main()
