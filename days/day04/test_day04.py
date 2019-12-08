import unittest
from day04 import check_increasing, check_double

class MyTestCase(unittest.TestCase):
    def test_check_double(self):
        self.assertTrue(check_double("110405"))
        self.assertTrue(check_double("123455"))
        self.assertTrue(check_double("123356"))
        self.assertTrue(check_double("111111"))
        self.assertFalse(check_double("123456"))
        self.assertFalse(check_double("123456789"))

    def test_check_increasing(self):
        self.assertTrue(check_increasing("123356"))
        self.assertTrue(check_increasing("111111"))
        self.assertTrue(check_increasing("12349"))
        self.assertTrue(check_increasing("123789"))
        self.assertFalse(check_increasing("913945"))
        self.assertFalse(check_increasing("223450"))



if __name__ == '__main__':
    unittest.main()
