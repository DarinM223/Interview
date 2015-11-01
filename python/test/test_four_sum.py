import unittest
import src.four_sum as mod

class TestFourSum(unittest.TestCase):
    def testNormalCase(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        result = mod.four_sum(test_input, 20)
        self.assertEqual(sorted(result), [2, 3, 7, 8])

    def testAllDuplicates(self):
        test_input = [2, 2, 2, 2, 2]
        result = mod.four_sum(test_input, 8)
        self.assertIsNone(result)

