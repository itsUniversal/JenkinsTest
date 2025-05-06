# test_sample.py
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

    def test_fail(self):
        self.assertEqual(5 - 3, 1)  # This will fail on purpose

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner())
