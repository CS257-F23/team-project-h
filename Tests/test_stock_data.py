from ProductionCode.stock_data import *
from test_data import *
import unittest
import subprocess


class TestBasic_cl(unittest.TestCase):

    # def setUp(self):
    #     targetList = ["NFLX", "GOOG", "AMZN", "MSFT", "FB", "GE", "CMCSA", "WFC", "MAR", "JPM"]
    #     companyData = setup(targetList)

    def test_get_by_company(self):
        """Test to check the data is filtered by company correctly"""

        test_company_data = {"NFLX" : {'2020-04-01' : "111", '2020-04-02' : "222"},"GOOG" : {'2020-04-01' : "111", '2020-04-02' : "222"}, "AMZN" : {'2020-04-01' : "111", '2020-04-02' : "222"}}
        arguments = ["NFLX", "AMZN"]
        filteredData = {"NFLX" : {'2020-04-01' : "1q11", '2020-04-02' : "222"}, "AMZN" : {'2020-04-01' : "111", '2020-04-02' : "222"}}

        data = get_by_company(test_company_data, arguments)

        self.assertEqual(data, filteredData)

    def test_get_by_date(self):
        test_company_data = {"NFLX" : {'2020-04-01' : "111", '2020-04-02' : "222"},"GOOG" : {'2020-04-01' : "111", '2020-04-02' : "222"}, "AMZN" : {'2020-04-01' : "111", '2020-04-02' : "222"}}
        arguments = ["2020-04-01"]
        filteredData = {"NFLX" : {'2020-04-01' : "111"},"GOOG" : {'2020-04-01' : "111"}, "AMZN" : {'2020-04-01' : "111"}}
        
        data = get_by_date(test_company_data, arguments)

        self.assertEqual(data, filteredData)

    def test_edge_get_by_date(self):
        test_company_data = {"NFLX" : {'2020-04-01' : "111", '2020-04-02' : "222"},"GOOG" : {'2020-04-01' : "111", '2020-04-02' : "222"}, "AMZN" : {'2020-04-01' : "111", '2020-04-02' : "222"}}
        arguments = ["not a date"]
        
        data = get_by_date(test_company_data, arguments)

        self.assertEqual(data, None)

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
        test_company_data = {"NFLX" : {'2020-04-01' : "111", '2020-04-02' : "222"},"GOOG" : {'2020-04-01' : "111", '2020-04-02' : "222"}, "AMZN" : {'2020-04-01' : "111", '2020-04-02' : "222"}}
        empty_data = {}
        companyData = {}
        test_data = get_all(load(["NFLX", "GOOG", "AMZN", "MSFT", "FB", "GE", "CMCSA", "WFC", "MAR", "JPM"], companyData))

        self.assertEqual(get_all(test_company_data), test_company_data)
        self.assertEqual(get_all(empty_data), empty_data)
        self.assertEqual(len(test_data), 10)
        
    def test_get_help(self):
        '''Test to see if the get_help function runs '''

        self.assertEqual(get_help(), True)



if __name__ == '__main__':
    unittest.main()
