import unittest

from .day01 import calc_fuel, part1, part2, slurp


class TestDay1(unittest.TestCase):
    def setUp(self):
        self.data = slurp()

    def test_part1(self):
        self.assertEqual(part1(self.data), 3182375)

    def test_part2(self):
        self.assertEqual(part2(self.data), 4770725)

    def test_calc(self):
        self.assertEqual(calc_fuel(14), 2)


if __name__ == '__main__':
    unittest.main()
