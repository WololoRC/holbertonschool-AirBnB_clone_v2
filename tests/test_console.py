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
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """some"""
        del cls.consol

    def tearDown(self):
        """some"""
        try:
            os.remove('file.json')
        except Exception:
            pass
    
    def test_emptyline(self):
        """some"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())
    
    def test_quit(self):
        """some"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())
            
    def test_create(self):
        """some"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

if __name__ == '__main__':
    unittest.main()
