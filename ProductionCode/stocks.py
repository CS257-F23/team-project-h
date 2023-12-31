import sys
import os
from ProductionCode.datasource import *


class Stocks():

    def get_data(self, companyList, dateList):
        ''' Purpose: Fetches data from the query based on a list of companies and dates. 
        Arguments: list of companies and list of dates from the user 
        '''
        if isEmpty(companyList):  
            return []
        data = DataSource()
        filteredData = data.fetch_data(tuple(companyList), tuple(dateList))
        return self.format_data(filteredData)


    def format_data(self, filteredData): ## helper function of get_data()
        ''' Purpose: takes in list of tuples and formats it into nested dictionary 
        Arguments: data (list of tuples) 
        Returns: dictionary
        '''
        companyData = {}
        for row in filteredData:
            if row[0] not in companyData:
                companyData[row[0]] = {}
            companyData[row[0]][row[1]] = row[2]
        return companyData
    

    def get_all_data(self):
        '''
        Purpose: gets all the companies (so that the query is only called once)
        Return: dictionary 
        '''
        companyList = ["AMZN", "CMCSA", "FB", "GE", "GOOG" ,"JPM", "MAR", "MSFT", "NFLX", "WFC"]
        return self.get_data(companyList, ())

    def get_help(self):
        """
        This function helps the user use the app. 
        """
        printStatement = ("\n¯\_(ツ)_/¯ \n Hey! To print out all stocks for a specific company, type in --get_company [company name]" +
            "\n To print out stocks for a company on by a specific date, type in --get_on_date [company name] [date]" +
            "\n These are the possible company names: NFLX, GOOG, AMZN, MSFT, FB, GE, CMCSA, WFC, MAR, JPM" +
            "\n This is the possible data range: 2019-04-01 - 2020-04-01.\n")
        return printStatement

    
