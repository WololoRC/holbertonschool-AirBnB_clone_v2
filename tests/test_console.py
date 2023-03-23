#!/usr/bin/python3
"""
test console
"""
import os
from unittest.mock import patch
from io import StringIO
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """some"""

    @classmethod
    def setClass(cls):
        """set up test"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def teardown(cls):
        """some"""
        del cls.HBNB

    def tearDown(cls):
        """some"""
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB
    
    def test_emptyline(self):
        """some"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual('', f.getvalue())
    
    def test_quit(self):
        """some"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual('', f.getvalue())
            
    def test_create(self):
        """some"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())

if __name__ == '__main__':
    unittest.main()
