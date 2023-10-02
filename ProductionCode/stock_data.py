import sys
import os

"""""
Check, load, and setup functions are used to load the data from the Data subdictionary 
"""
def check(targetList) -> bool:
    companies = os.listdir("Data/")
    companyList = []
    for company in companies:
        companyList.append(company.split(".")[0])
    for target in targetList:
        if target not in companyList:
            return False
    return True

def load(targetList, companyData) -> dict:
    for target in targetList:
        company = {}
        dates = ((open("Data/"+target+".csv", "r")).read()).split("\n")
        for date in dates:
            try:
                date = date.split(",")
                company[date[0]] = date[4]
            except:
                pass
        companyData[target] = company
    return companyData

def setup(targetList) -> dict:
    if check(targetList):
        companyData = {}
        load(targetList, companyData)
        return companyData
    else:
        print("data anomoly")
        return None
    
def print_data(companyData):
    """
    This function is used to print the data in the main function. 
    """
    for companyName, data in companyData.items():
        print(" ")
        print(companyName + " Historical Stock Data")
        for date, value in data.items():
            print(date, ":", value)
    

def get_all(companyData) -> dict:
    """
    This returns all the data stored in company data for all companies and all dates.   
    """
    if len(companyData) == 0:
        print("Please check your Data file. The dictionary is empty!")
    return companyData


def get_by_company(companyData, arguments) -> dict:
    """Filters the all company stock data by company inputed by user

    Args:
        companyData (dict): all company stock data
        arguments (list): list of command line arguments

    Returns:
        dict: filtered dict of company data
    """
    filteredCompanyData = {}
    for key in companyData:
        if key in arguments:
            filteredCompanyData[key] = companyData[key]
    return filteredCompanyData

def get_by_date(companyData, arguments) -> dict:
    """
    This function returns the values on a specific date for all the 10 companies. 
    """
    final = {}
    dateList = arguments[2].split(",")
    if len(dateList) < 1:
        print("erroneous input")
        return final
    companies = companyData.keys()
    for company in companies:
        final[company] = {}
    try:
        for date in dateList:
            for company in companies:
                final[company][date] = companyData[company][date]
    except:
        print("erroneous data")
    return final

def get_help():
    """
    This function helps the user use the app. 
    """
    print("")
    print("¯\_(ツ)_/¯")
    print("Hey! To print out stocks for a specific company, type in --get_by_company [company name]")
    print("To print out stocks by a specific date, type in --get_by_date [date]")
    print("These are the possible company names: NFLX, GOOG, AMZN, MSFT, FB, GE, CMCSA, WFC, MAR, JPM")
    print("This is the possible data range: 2019-04-01 - 2020-04-01.")
    print("")


def main():
    #list of all company codes to be parsed
    targetList = ["NFLX", "GOOG", "AMZN", "MSFT", "FB", "GE", "CMCSA", "WFC", "MAR", "JPM"]
    companyData = setup(targetList)
    if companyData == None:
        return

    arguments = sys.argv
    try:
        if arguments[1] == "--get_all":
            data = get_all(companyData)
            print_data(data)
        elif arguments[1] == "--get_by_company":
            data = get_by_company(companyData, arguments)
            print_data(data)
        elif arguments[1] == "--get_by_date":
            data = get_by_date(companyData, arguments)
            print_data(data)
        elif arguments[1] == "--get_h" or "--get_help":
            get_help()
    except:
        print("Error. Please give more arguments. You can call the --get_help function to see what arguments to include.")

if __name__ == "__main__":
    main()