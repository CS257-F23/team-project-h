from ProductionCode.stocks import *
import unittest
import subprocess
import imp

stock = Stocks()

class TestBasic_cl(unittest.TestCase):
    
    def test_predict(self):
        '''This tests if the predict function returns correct rounded values for user inputs '''
        userIn = {"NFLX": "1.0", "GOOG": "2.0", "AMZN": "3.0"}
        self.assertEqual(stock.predict(userIn), (6.0, 6.0, 0.0))

    def test_predict_edge(self):
        '''This tests that non-digit inputs do not work and return 0.0'''
        userIn = {"NFLX": "not digits", "GOOG":"not digits", "AMZN":"not digits"}
        self.assertEqual(stock.predict(userIn), (0.0, 0.0, 0.0))

    def test_get_data(self):
        pass

    def test_format_data(self):
        testInput = [("NFLX", "2020-04-04", 100),("GOOG", "2020-04-04", 100)]  

        res = stock.format_data(testInput)

        expectedResult = {"NFLX" : {"2020-04-04" : 100}, "GOOG" : {"2020-04-04" : 100}}

        self.assertEqual(res, expectedResult)


    def test_get_all_data(self):
        pass

    def test_get_data_edge(self):
        pass

    def test_format_data_edge(self):
        pass        

    def test_get_all_data_edge(self):
        pass
        
    

if __name__ == '__main__':
    unittest.main()
