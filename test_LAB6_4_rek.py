import unittest
from LAB6_4_rek import last_positive_index

a = [-1, 48, 50, 14, 0, -5, -7, -6, 45, 0, 0, 1, 2, 3, 31]


class TestLAB64it(unittest.TestCase):
    def test_last_positive_index(self):
        self.assertEqual(last_positive_index(a, 14), 14)  # add assertion here


if __name__ == '__main__':
    unittest.main()
