import unittest
from cl_app import *
import subprocess

class TestClApp(unittest.TestCase):

    def test_get_company(self):
        '''Test get_company() function; should return the value of stock for all dates as a string. '''

        code = subprocess.Popen(['python3', '-u', 'cl_app.py', "--get_company", 'GOOG'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                encoding='utf8')
        
        output, err = code.communicate()
        self.assertIn("{'GOOG': {'2019-04-01': 1194.43, '2019-04-02': 1200.49, '2019-04-03': 1205.92", output.strip())
        code.terminate()
    

    def test_edge_get_company(self):
        '''Test get_company() edge case for invalid company name "HELLO"; should return string "Invalid Input". '''

        code = subprocess.Popen(['python3', '-u', 'cl_app.py', "--get_company", 'HELLO'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                encoding='utf8')
        
        output, err = code.communicate()
        self.assertIn("Invalid Input", output.strip())
        code.terminate()


    def test_get_on_date(self):
        '''Test get_on_date() function; should return the value of stock on that date as a string. '''

        code = subprocess.Popen(['python3', '-u', 'cl_app.py', "--get_on_date", 'NFLX', "2020-04-01"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                encoding='utf8')
        
        output, err = code.communicate()
        self.assertEqual("{'NFLX': {'2020-04-01': 364.08}}", output.strip())
        code.terminate()


    def test_edge_get_on_date(self):
        '''Test get_on_date() edge case for invalid date 2040-04-01; should return the string "Invalid Input". '''

        code = subprocess.Popen(['python3', '-u', 'cl_app.py', "--get_on_date", 'NFLX', "2040-04-01"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                encoding='utf8')
        
        output, err = code.communicate()
        self.assertEqual("Invalid Input", output.strip())
        code.terminate()


    def test_get_help(self):
        '''Test get_help() function; should return usage statement.'''

        code = subprocess.Popen(['python3', '-u', 'cl_app.py', "--get_h"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                encoding='utf8')
        
        output, err = code.communicate()
        self.assertIn("Hey! To print out all stocks for a specific company, type in --get_company [company name]", output.strip())
        code.terminate()


if __name__ == "__main__":
    unittest.main()