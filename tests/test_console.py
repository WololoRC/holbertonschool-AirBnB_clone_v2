#!/usr/bin/python3
"""
test console
"""
import os
from unittest.mock import patch
from io import StringIO
import unittest
from console import HBNBCommand


class testConsole(unittest.TestCase):
    """some"""

    def setClass(cls):
        """set up test"""
        cls.consol = HBNBCommand()

    def tearDown(self) -> None:
        return super().tearDown()
    
    def tear_down(cls):
        del cls.consol

    def tear_Down(self):
        try:
            os.remove('file.json')
        except Exception:
            pass
    
    def test_emptyline(self):
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