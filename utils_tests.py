import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    def test_reversed_integer(self):
        self.assertEqual(Utils.reversed(12345), 54321)

    def test_reversed_float(self):
        with self.assertRaises(ValueError):
            Utils.reversed(12.34)

    def test_reversed_string(self):
        with self.assertRaises(ValueError):
            Utils.reversed("12345")

    def test_formatter_integer(self):
        binary, octal = Utils.formatter(42)
        self.assertEqual(binary, '0b101010')
        self.assertEqual(octal, '0o52')

    def test_formatter_float(self):
        with self.assertRaises(ValueError):
            Utils.formatter(3.14)

    def test_formatter_string(self):
        with self.assertRaises(ValueError):
            Utils.formatter("42")

if __name__ == '__main__':
    unittest.main()

