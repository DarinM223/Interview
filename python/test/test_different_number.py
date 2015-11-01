import unittest
import sys
from src import different_number as mod

class TestDifferentNumber(unittest.TestCase):
    def testNormal(self):
        test_input = [-sys.maxint - 1, -1, 1, 3, 4, 6, 7, 8, 9, sys.maxint]
        self.assertEqual(mod.different_number(test_input, len(test_input)), 0)
    
