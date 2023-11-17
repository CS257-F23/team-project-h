import unittest
from ProductionCode.datasource import *
from data import *

class TestDataSource(unittest.TestCase):

    def test_fetch_data(self):
        '''Purpose: Test for fetch_data() function; should return correct data from the query for 2 dates and 2 companies.'''
        data = DataSource()
        companyTuple = ("GOOG", "AMZN")
        dateTuple = ("2019-04-01", "2020-04-01")
        result = data.fetch_data(companyTuple, dateTuple)
        expectedResult = [('AMZN', '2019-04-01', 1814.19), ('AMZN', '2020-04-01', 1907.7), ('GOOG', '2019-04-01', 1194.43), ('GOOG', '2020-04-01', 1105.62)]
        self.assertEqual(result, expectedResult)

    def test_fetch_data_edge(self):
        '''Purpose: Test for an edge case of fetch_data() on an invalid date; should return an empty list'''
        data = DataSource()
        companyTuple = ("GOOG", "AMZN")
        dateTuple = ("2025-04-01",)
        result = data.fetch_data(companyTuple, dateTuple)
        self.assertEqual(result, [])

    def test_fetch_only_companies(self):
        '''Purpose: Test fetch_only_companies() function for 2 companies; should all stock data for the 2 companies'''
        data = DataSource()
        companyTuple = ("GOOG", "AMZN")
        result = data.fetch_only_companies(companyTuple)
        self.assertEqual(result, testData) #complete testData is in data.py file 
        
    def test_fetch_companies_and_dates(self):
        '''Purpose: Test fetch_companies_and_dates() function for 2 companies and 2 dates; should return data for those parameters'''
        data = DataSource()
        companyTuple = ("GOOG", "AMZN")
        dateTuple = ("2019-04-01", "2020-04-01")
        result = data.fetch_companies_and_dates(companyTuple, dateTuple)
        expectedResult = [('AMZN', '2019-04-01', 1814.19), ('AMZN', '2020-04-01', 1907.7), ('GOOG', '2019-04-01', 1194.43), ('GOOG', '2020-04-01', 1105.62)]
        self.assertEqual(result, expectedResult)

    def test_fetch_only_companies_edge(self):
        '''Purpose: Test edge case for fetch_only_companies() for an invalid company; should return an empty list'''
        data = DataSource()
        companyTuple = ("not a company",)
        result = data.fetch_only_companies(companyTuple)
        self.assertEqual(result, [])

    def test_fetch_companies_and_dates_edge(self):
        '''Purpose: Test for an edge case of fetch_companies_and_dates() for invalid dates; should return an empty list'''
        data = DataSource()
        companyTuple = ("GOOG", "AMZN")
        dateTuple = ("2027-04-01", "2028-04-01")
        result = data.fetch_companies_and_dates(companyTuple, dateTuple)
        self.maxDiff = None
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()