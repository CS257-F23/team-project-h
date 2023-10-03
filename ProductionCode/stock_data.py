import sys
import os


def check(targetList) -> bool:
    companies = os.listdir("data/")
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
        dates = ((open("data/"+target+".csv", "r")).read()).split("\n")
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
    for companyName, data in companyData.items():
        print(" ")
        print(companyName + " Historical Stock Data")
        for date, value in data.items():
            print(date, ":", value)
    

def get_all(companyData) -> dict:
    for company in companyData.key():
        print(company, ":", companyData[company])
    pass

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
    final = {}
    dateList = arguments[2].split(",")
    if len(dateList) < 1:
        print("erroneous input")
        return final
    companies = companyData.keys()
    for company in companies:
        final[company] = {};
    try:
        for date in dateList:
            for company in companies:
                final[company][date] = companyData[company][date]
    except:
        return None
    return final

def get_help():
    print("Hey, to print out stocks for a company, type in --get_by_company [company name]")
    print("To print out stocks by date, type in --get_by_date [date]")
    print("These are the possible company names: NFLX, GOOG, AMZN, MSFT, FB, GE, CMCSA, WFC, MAR, JPM")


def main():
    #list of all company codes to be parsed
    targetList = ["NFLX", "GOOG", "AMZN", "MSFT", "FB", "GE", "CMCSA", "WFC", "MAR", "JPM"]
    companyData = setup(targetList)
    if companyData == None:
        return

    arguments = sys.argv
    try:
        if arguments[1] == "--get_all":
            get_all(companyData)
        elif arguments[1] == "--get_by_company":
            data = get_by_company(companyData, arguments)
            print_data(data)
        elif arguments[1] == "--get_by_date":
            get_by_date(companyData, arguments)
        elif arguments[1] == "--get_h":
            get_help()
    except:
        print("error")

if __name__ == "__main__":
    main()