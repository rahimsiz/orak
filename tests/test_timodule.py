import unittest
from tirpan.timodule import Timodule
import imp

class TestTimodule(unittest.TestCase):

    def test_load_path(self):
        self.assertEqual(Timodule('ast').path, imp.find_module('ast')[1])
        self.assertIsNone(Timodule('_ast').path)
        path = '/test/path/filename.py'
        self.assertEqual(Timodule('__main__', None, path).path, path)

    def test_is_buildin_method(self):
        self.assertFalse(Timodule('ast').is_buildin())
        self.assertTrue(Timodule('_ast').is_buildin())
        self.assertFalse(Timodule('__main__', None, '/test/path/filename.py').is_buildin())
