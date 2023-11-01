import sys
import os
from ProductionCode.datasource import *


class Stocks():
    # def __init__(self): 
    #     # self.allCompaniesData = self.load()
        
    # """
    # Check, load, and setup functions are used to load the data from the Data subdictionary 
    # """

    # def load(self) -> dict:
    #     """ This creates the overall dictionary of target companies 

    #     Returns:
    #         dict: _description_
    #     """
    #     targetList = ["NFLX", "GOOG", "AMZN", "MSFT", "FB", "GE", "CMCSA", "WFC", "MAR", "JPM"]
    #     allCompaniesData = {}
    #     for target in targetList:
    #         dates = ((open("Data/"+target+".csv", "r")).read()).split("\n")
    #         allCompaniesData[target] = self.load_helper(dates)
    #     return allCompaniesData


    # def load_helper(self, dates):
    #     """  

    #     Returns:
    #         dict: _description_
    #     """
    #     company = {}
    #     for rowOfData in dates:
    #         rowOfData = rowOfData.split(",")
    #         company[rowOfData[0]] = rowOfData[4]
    #     return company

    # def print_data(self, allData):
    #     """
    #     This function is used to print the data in the main function. 
    #     """
    #     if allData == None:
    #         return None
    #     for companyName, data in allData.items():
    #         print(" ")
    #         print(companyName + " Historical Stock Data")
    #         for date, value in data.items():
    #             print(date, ":", value)

    # def get_by_company(self, arguments, filteredData = {}) -> dict:
    #     """Filters the all company stock data by company inputed by user

    #     Args:
    #         allCompaniesData (dict): all company stock data
    #         arguments (list): list of command line arguments

    #     Returns:
    #         dict: filtered dict of company data
    #     """
    #     if filteredData == {}:
    #         filteredData = self.allCompaniesData
    #     filteredCompanyData = {}
    #     for key in filteredData:
    #         if key in arguments:
    #             filteredCompanyData[key] = filteredData[key]
    #     return filteredCompanyData


    # def get_by_date(self, arguments, filteredData = {}) -> dict: 
    #     """ This function returns the values on a specific date for all the 10 companies. """ 
    #     if filteredData == {}:
    #         filteredData = self.allCompaniesData
    #     filteredCompanyData = {} 
    #     for company in filteredData: 
    #         filteredCompanyData[company] = {}
    #         self.get_by_date_helper(company, arguments, filteredCompanyData)
    #     return filteredCompanyData


    # def get_by_date_helper(self, company, arguments, filteredCompanyData):
    #     """This helps handle if the user inputs multiple dates 

    #     Args:
    #         allCompaniesData (_type_): _description_
    #         company (_type_): _description_
    #         arguments (_type_): _description_
    #         filteredallCompaniesData (_type_): _description_
    #     """

    #     for date in arguments: 
    #         if date in self.allCompaniesData[company]:
    #             filteredCompanyData[company][date] = self.allCompaniesData[company][date]

    def get_data(self, companyList, dateList):
        data = DataSource()
        filteredData = data.get_data(tuple(companyList), tuple(dateList))
        companyData = {}
        for row in filteredData:
            if row[0] not in companyData:
                companyData[row[0]] = {}
            companyData[row[0]][row[1]] = row[2]
        return companyData

    def get_help(self):
        """
        This function helps the user use the app. 
        """
        print("\n¯\_(ツ)_/¯ \n Hey! To print out stocks for a specific company, type in --get_by_company [company name]" +
            "\n To print out stocks by a specific date, type in --get_by_date [date]" +
            "\n These are the possible company names: NFLX, GOOG, AMZN, MSFT, FB, GE, CMCSA, WFC, MAR, JPM" +
            "\n This is the possible data range: 2019-04-01 - 2020-04-01.\n")
        return True
    
    def predict(self, userIn):
        """This function predicts how much the stocks will earn/lose based on user investment.

        Args:
            userIn (dict): User investment input

        Returns:
            tuple: returns the initial investment amount, final investment amount, and the difference.
        """
        initial = 0.0
        final = 0.0
        if userIn == None:
            return None
        try:
            for companyValue in userIn:
        
                initial += float(userIn[companyValue])
                factor = float(self.allCompaniesData[companyValue]["2020-04-01"]) / float(self.allCompaniesData[companyValue]["2019-04-01"])
                final += float(userIn[companyValue]) * factor
        except:
            pass
        final = round(final, 2)
        return (initial, final, final-initial)
