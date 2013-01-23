import unittest
import orak

class TestOrakFuncCall(unittest.TestCase):

    def test_simple_args(self):
        self.assertTrue(orak.Orak("tests/files/orak_func_call/simple_args_safe.py").check())
        self.assertFalse(orak.Orak("tests/files/orak_func_call/simple_args_unsafe.py").check())

    def test_assigned_func(self):
        self.assertTrue(orak.Orak("tests/files/orak_func_call/assigned_func_call_safe.py").check())
        self.assertFalse(orak.Orak("tests/files/orak_func_call/assigned_func_call_unsafe.py").check())
