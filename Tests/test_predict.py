from ProductionCode.predict import *
import unittest

data = Predict()
class TestPredict(unittest.TestCase):

    def test_predict(self):
        '''Purpose: Test the predict function; should return correct rounded values for user inputs '''
        userIn = {"NFLX": "1.0", "GOOG": "2.0", "AMZN": "3.0"}
        self.assertEqual(data.predict(userIn), (6.0, 6.0, 0.0))

    def test_predict_edge(self):
        '''Purpose: Tests edge case of predict class for non-digit inputs; should return 0.0'''
        userIn = {"NFLX": "not digits", "GOOG":"not digits", "AMZN":"not digits"}
        self.assertEqual(data.predict(userIn), (0.0, 0.0, 0.0))