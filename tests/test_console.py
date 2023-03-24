#!/usr/bin/python3
"""unit test"""

import unittest
from io import StringIO
from unittest import patch


class TestConsole(unittest.TestCase):
    
    def test_emptyline(self):
        """Test empty line input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCommand().onecmd("\n")
            self.assertEqual("", f.getvalue())