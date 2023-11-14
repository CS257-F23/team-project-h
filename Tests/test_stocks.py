from ProductionCode.stocks import *
import unittest
import subprocess
import imp

stock = Stocks()

class TestBasic_cl(unittest.TestCase):

    def test_get_data(self):
        '''Purpose: Test get_data() function on 2 companies and 2 dates; should return correctly-formatted (in dictionaries) fetched data.'''
        compList = ["NFLX", "GOOG"]
        dateList = ["2019-04-01", "2020-04-01"]
        result = stock.get_data(compList, dateList)
        expectedResult = {'GOOG': {'2019-04-01': 1194.43, '2020-04-01': 1105.62}, 'NFLX': {'2019-04-01': 366.96, '2020-04-01': 364.08}}
        self.assertEqual(result, expectedResult)

    def test_format_data(self):
        '''Purpose: Test for format_data() function; takes in tuples, should return formatted dictionaries'''
        testInput = [("NFLX", "2020-04-04", 100),("GOOG", "2020-04-04", 100)]  
        res = stock.format_data(testInput)
        expectedResult = {"NFLX" : {"2020-04-04" : 100}, "GOOG" : {"2020-04-04" : 100}}
        self.assertEqual(res, expectedResult)


    def test_get_all_data(self):
        '''Purpose: Test for get_all_data(); should return 10 dictionaries (1 for each company), and 254 dictionaries for each company. '''
        result = stock.get_all_data()
        self.assertEqual(len(result), 10) 
        self.assertEqual(len(result["GOOG"]), 254)


    def test_get_data_edge(self):
        '''Purpose: Test get_data() function on 2 companies and 2 dates; should return correctly-formatted (in dictionaries) fetched data.'''
        compList = ["not a company"]
        dateList = ["not a date"]
        result = stock.get_data(compList, dateList)
        expectedResult = {}
        self.assertEqual(result, expectedResult)


    def test_format_data_edge(self):
        '''Purpose: Test for format_data() edge case of an empty list passed in; should format and return empty dictionary'''
        self.assertEqual(stock.format_data([]), {})
        
    

if __name__ == '__main__':
    unittest.main()
