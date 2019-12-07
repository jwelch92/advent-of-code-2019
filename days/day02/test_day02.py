import unittest

from day02 import part1


# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

class MyTestCase(unittest.TestCase):
    def test_simple_add(self):
        self.assertEqual(part1([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])

    def test_simple_mult(self):
        self.assertEqual(part1([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])

    def test_mult(self):
        self.assertEqual(part1([2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801])

    def test_longer(self):
        self.assertEqual(part1([1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99])


if __name__ == '__main__':
    unittest.main()
