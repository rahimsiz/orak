__author__ = 'ramil'
import unittest
import orak

class TestOrakClassInit(unittest.TestCase):

    def test_simple_class(self):
        self.assertFalse(orak.Orak("tests/files/orak_class_init/simple_class.py").check())

    def test_inherited_class(self):
        self.assertFalse(orak.Orak("tests/files/orak_class_init/inherited_class.py").check())
