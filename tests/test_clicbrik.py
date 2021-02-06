from bricklee import __version__
from bricklee.entrypoint import main
import unittest

class TestClicBrik(unittest.TestCase):
    def test_version_010(self):
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