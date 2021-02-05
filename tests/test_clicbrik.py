from clicbrik import __version__
import unittest

def test_version():
    assert __version__ == '0.1.0'

class TestClicBrik(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, '0.1.0')

if __name__ == '__main__':
    unittest.main()