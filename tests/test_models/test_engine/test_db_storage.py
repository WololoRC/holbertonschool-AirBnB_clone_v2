#!/usr/bin/python3
""" base model, models """

import unittest
from console import HBNBCommand


class TestDBstorage(unittest.TestCase):
    """ """
    def create(self):
        """some"""
        return HBNBCommand()    


if __name__ == '__main__':
    unittest.main()
