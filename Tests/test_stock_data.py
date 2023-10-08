from ProductionCode.stock_data import *
from test_data import *
import unittest
import subprocess


class TestBasic_cl(unittest.TestCase):

    ''' testData is the smaller dataset we will be testing on'''
    testData = {"NFLX" : {'2020-04-01' : "111", '2020-04-02' : "222"},
             "GOOG" : {'2020-04-01' : "111", '2020-04-02' : "222"}, 
             "AMZN" : {'2020-04-01' : "111", '2020-04-02' : "222"}}
    
    def test_get_by_company(self):
        """Test to check the data is filtered by company correctly"""
        arguments = ["NFLX", "AMZN"]
        filteredData = {"NFLX" : {'2020-04-01' : "111", '2020-04-02' : "222"}, 
                        "AMZN" : {'2020-04-01' : "111", '2020-04-02' : "222"}}

        data = get_by_company(self.testData, arguments)

        self.assertEqual(data, filteredData)

    def test_false_company(self):
        "This tests if an incorrect name is passed into get by company"
        arguments = "BOB"

        data = get_by_company(self.testData, arguments)

        self.assertEqual(data, {})


    def test_get_by_date(self):
        '''This tests that get by date returns stock data for all companies on a specific date'''
        arguments = ["blank", "blank", "2020-04-01"] 
        filteredData = {"NFLX" : {'2020-04-01' : "111"},
                        "GOOG" : {'2020-04-01' : "111"}, 
                        "AMZN" : {'2020-04-01' : "111"}}
        
        data = get_by_date(self.testData, arguments)

        self.assertEqual(data, filteredData)


    def test_edge_get_by_date(self):
        '''This tests if a user puts in invalid input for a date '''
        arguments = ["blank", "blank", "not a date"]
        filteredData = {'NFLX': {}, 'GOOG': {}, 'AMZN': {}} 
        
        data = get_by_date(self.testData, arguments)

        self.assertEqual(data, filteredData)


    def test_print_data(self):
        """Test to check the data is printed correctly"""

        expected_company1 = "NFLX"
        expected_company2 = "AMZN"

        code = subprocess.Popen(['python3', '-u', 'ProductionCode/stock_data.py', "--get_by_company", 'NFLX', "AMZN"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                encoding='utf8')
        
        output, err = code.communicate()

        self.assertIn(expected_company1, output.strip())
        self.assertIn(expected_company2, output.strip())

        code.terminate()
    

    def test_get_all(self):
        '''Test to see if the function returns the entire dataset'''
        test_data = get_all(self.testData)

        self.assertEqual(test_data, self.testData)


    def test_get_all_empty_data(self):
        '''This tests an empty data set'''
        empty_data = {}

        self.assertEqual(get_all(empty_data), empty_data)


    def test_load_data(self):
        '''This tests load on the the entire data set'''

        self.assertEqual(len(load()), 10)
        

    def test_get_help(self):
        '''Test to see if the get_help function runs '''

        self.assertEqual(get_help(), True)



if __name__ == '__main__':
    unittest.main()
