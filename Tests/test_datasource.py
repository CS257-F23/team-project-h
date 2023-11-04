import unittest
from ProductionCode.datasource import *

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
        '''Purpose: Test for an edge case of fetch_data() on an empty input; should return an empty list'''
        data = DataSource()
        companyTuple = ()
        dateTuple = ()
        result = data.fetch_data(companyTuple, dateTuple)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()