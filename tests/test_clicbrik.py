from clicbrik import __version__
import unittest
from clicbrik.entrypoint import main

class TestClicBrik(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, '0.1.0')
        
    def test_generic_hello(self):
        expected = 'Hello Panama City, Panama.'
        actual = main(['hello'])
        self.assertEqual(actual, expected)

    def test_customized_hello(self):
        expected = 'Hello Adriaan.'
        actual = main(['hello', '--name', 'Adriaan'])
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()