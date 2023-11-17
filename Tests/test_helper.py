import unittest
from ProductionCode.helper import *

class TestHelper(unittest.TestCase):

    def test_isEmpty_true(self):
        '''Purpose: Tests isEmpty() helper function; should return True on an emtpy list'''
        self.assertEqual(True, isEmpty([]))

    def test_isEmpty_false(self):
        '''Purpose: Tests isEmpty() helper function; should return False on non-empty list'''
        self.assertEqual(False, isEmpty([1,2,3]))

if __name__ == "__main__":
    unittest.main()