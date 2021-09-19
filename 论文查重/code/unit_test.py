import unittest
from main import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main(), 0.99)  # add assertion here


if __name__ == '__main__':
    unittest.main()
