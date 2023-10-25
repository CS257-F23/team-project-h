from ProductionCode.cl import *
from cl_app import *
import unittest
import subprocess
import imp

stock = Stocks()

class TestBasic_cl(unittest.TestCase):
    def setUp(self):

        ''' testData is the smaller dataset we will be testing on'''
        self.testData = {"NFLX" : {'2020-04-01' : "111", '2020-04-02' : "222"},
             "GOOG" : {'2020-04-01' : "111", '2020-04-02' : "222"}, 
             "AMZN" : {'2020-04-01' : "111", '2020-04-02' : "222"}}
    

    def test_get_by_company(self):
        '''Test to check the data is filtered by company correctly'''
        arguments = ["NFLX", "AMZN"]
        filteredData = {"NFLX" : {'2020-04-01' : "111", '2020-04-02' : "222"}, 
                        "AMZN" : {'2020-04-01' : "111", '2020-04-02' : "222"}}

        data = stock.get_by_company(arguments, self.testData)

        self.assertEqual(data, filteredData)

    def test_false_company(self):
        '''Test for an edge case of get_by_company, if an incorrect name is passed in.'''
        arguments = "BOB"

        data = stock.get_by_company(arguments, self.testData)

        self.assertEqual(data, {})


    def test_get_by_date(self):
        '''Test for get_by_date that should return stock data for all companies on a specific date'''
        arguments = ["2020-04-01"] 
        filteredData = {"NFLX" : {"2020-04-01" : "364.08"}, "GOOG" : {"2020-04-01" : '1105.62'}, "AMZN" : {"2020-04-01" : "1907.7"} }
        
        data = stock.get_by_date(arguments, self.testData)

        self.assertEqual(data, filteredData)


    def test_edge_get_by_date(self):
        '''Test for an edge case of get_by_date, if a user puts in invalid input for a date. '''
        arguments = ["not a date"]
        filteredData = {'NFLX': {}, 'GOOG': {}, 'AMZN': {}} 
        
        data = stock.get_by_date(arguments, self.testData)

        self.assertEqual(data, filteredData)

    def test_print_data(self):
        '''Test that data is printed correctly.'''

        expected_company1 = "NFLX"
        expected_company2 = "AMZN"

        code = subprocess.Popen(['python3', '-u', 'cl_app.py', "--get_by_company", 'NFLX', "AMZN"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                encoding='utf8')
        
        output, err = code.communicate()

        self.assertIn(expected_company1, output.strip())
        self.assertIn(expected_company2, output.strip())

        code.terminate()


    def test_edge_print_data(self):
        '''Test for edge case of print_data if no data is given.'''
        self.assertEquals(None, stock.print_data(None))
        

    def test_load_data(self):
        '''Test to load the entire data set'''

        self.assertEqual(len(stock.load()), 10)


    def test_load_helper(self):
        '''Test for a helper function of load'''
        sampleData = ["2020-04-01,0,0,0,0"]
        self.assertEqual(type(stock.load_helper(sampleData)), dict)
        

    def test_get_by_date_helper(self):
        '''Test of a helper function for get_by_date()'''
        filteredCompanyData = {}
        filteredCompanyData["NFLX"] = {}
        stock.get_by_date_helper("NFLX", [1,1,"2020-04-01"], filteredCompanyData)
        self.assertEqual(filteredCompanyData, {"NFLX":{'2020-04-01' : "364.08"}})


    def test_edge_get_by_date_helper(self):
        '''Test of a helper function edge case for get_by_date() - invalid date'''
        filteredCompanyData = {}
        filteredCompanyData["NFLX"] = {}
        stock.get_by_date_helper("NFLX", [1,1,"invalid_date"], filteredCompanyData)
        self.assertEqual(filteredCompanyData, {"NFLX":{}})

    def test_predict(self):
        '''This tests if the predict function returns correct rounded values for user inputs '''
        userIn = {"NFLX": "1.0", "GOOG": "2.0", "AMZN": "3.0"}
        self.assertEqual(stock.predict(userIn), (6.0, 6.0, 0.0))

    def test_predict_edge(self):
        '''This tests that non-digit inputs do not work and return 0.0'''
        userIn = {"NFLX": "not digits", "GOOG":"not digits", "AMZN":"not digits"}
        self.assertEqual(stock.predict(userIn), (0.0, 0.0, 0.0))


    def test_get_help(self):
        '''Test to see if the get_help function runs '''
        self.assertEqual(stock.get_help(), True)

    def test_get_help_main(self):
        '''Test get help command'''
        self.assertEquals(None, main([1, "--get_h"]))

    def test_get_by_company_main(self):
        '''Test get by company command'''
        self.assertEquals(None, main([1, "--get_by_company", ""]))

    def test_get_by_date_main(self):
        '''Test get by date command'''
        self.assertEquals(None, main([1, "--get_by_date"]))

    def test_edge_main(self):
        '''Test the edge case for main'''
        self.assertEqual(None, main([1]))
    
    def test_name_main(self):
        '''Test the main function'''
        #using the imp module because using import to load python functions was not working with the unittest module and coverage testing
        runpy = imp.load_source('cl_app.py', 'ProductionCode/cl.py')


if __name__ == '__main__':
    unittest.main()
