from bricklee import __version__
from bricklee.entrypoint import greet
import unittest

class TestClicBrik(unittest.TestCase):
    def test_generic_hello(self):
        expected = 'Hello Panama City, Panama.'
        name = None
        actual = greet(name)
        self.assertEqual(actual, expected)

    def test_customized_hello(self):
        expected = 'Hello Adriaan.'
        name = 'Adriaan'
        actual = greet(name)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
