import sys
import os

"""""
Check, load, and setup functions are used to load the data from the Data subdictionary 
"""

def load() -> dict:
    """ This creates the overall dictionary of target companies 

    Returns:
        dict: _description_
    """
    targetList = ["NFLX", "GOOG", "AMZN", "MSFT", "FB", "GE", "CMCSA", "WFC", "MAR", "JPM"]
    allCompaniesData = {}
    for target in targetList:
        dates = ((open("Data/"+target+".csv", "r")).read()).split("\n")
        allCompaniesData[target] = load_helper(dates)
    return allCompaniesData


def load_helper(dates):
    """  

    Returns:
        dict: _description_
    """
    company = {}
    for date in dates:
        date = date.split(",")
        company[date[0]] = (date[4], date[6])
    return company


def print_data(allCompaniesData):
    """
    This function is used to print the data in the main function. 
    """
    if allCompaniesData == None:
        return 
    for companyName, data in allCompaniesData.items():
        print(" ")
        print(companyName + " Historical Stock Data")
        for date, value in data.items():
            print(date, ":", value)
    

def get_all(allCompaniesData):
    """
    This returns all the data stored in company data for all companies and all dates.   
    """
    print_data(allCompaniesData)


def get_by_company(allCompaniesData, arguments) -> dict:
    """Filters the all company stock data by company inputed by user

    Args:
        allCompaniesData (dict): all company stock data
        arguments (list): list of command line arguments

    Returns:
        dict: filtered dict of company data
    """
    filteredCompanyData = {}
    for key in allCompaniesData:
        if key in arguments:
            filteredCompanyData[key] = allCompaniesData[key]
    return filteredCompanyData


def get_by_date(allCompaniesData, arguments) -> dict: 
    """ This function returns the values on a specific date for all the 10 companies. """ 
    if len(arguments) < 3:
        print("Please enter a specific date you want to see stocks for. If you want to see multiple dates, connect them by a comma :)")
        return
    filteredCompanyData = {} 
    for company in allCompaniesData: 
        filteredCompanyData[company] = {}
        get_by_date_helper(allCompaniesData, company, arguments, filteredCompanyData)
    return filteredCompanyData


def get_by_date_helper(allCompaniesData, company, arguments, filteredCompanyData):
    """This helps handle if the user inputs multiple dates 

    Args:
        allCompaniesData (_type_): _description_
        company (_type_): _description_
        arguments (_type_): _description_
        filteredallCompaniesData (_type_): _description_
    """

    for date in allCompaniesData[company]:
        for date in arguments[2].split(","): 
            filteredCompanyData[company][date] = allCompaniesData[company][date]


def get_help():
    """
    This function helps the user use the app. 
    """
    print("\n¯\_(ツ)_/¯ \n Hey! To print out stocks for a specific company, type in --get_by_company [company name]" +
        "\n To print out stocks by a specific date, type in --get_by_date [date]" +
        "\n These are the possible company names: NFLX, GOOG, AMZN, MSFT, FB, GE, CMCSA, WFC, MAR, JPM" +
        "\n This is the possible data range: 2019-04-01 - 2020-04-01.\n")
    return True


def main():
    #list of all company codes to be parsed
    data = {}
    allCompaniesData = load()

    arguments = sys.argv

    if len(arguments) < 2:
        print("Bad input. Please type in --get_h to see your options!")
        return

    match arguments[1]:
        case "--get_h":
            get_help()
        case "--get_all":
            get_all(allCompaniesData)
        case "--get_by_company":
            data = get_by_company(allCompaniesData, arguments)
        case "--get_by_date":
            data = get_by_date(allCompaniesData, arguments)
    print_data(data)

if __name__ == "__main__":
    main()