import unittest
from helper import add_numbers

class TestHelper(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
