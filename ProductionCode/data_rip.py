"""
- run from the archive directory
- include desired companies to targetList
- change the number of dates returned at line 32 but u dont need to bc its alr a year
- will create corresponding csv files to ./results
- no data cleaning implemented, but can be added to data_correction()
"""

import os

def check_list_of_companies(targetList) -> bool:
    companies = os.listdir("stocks/")
    companyList = []
    for company in companies:
        companyList.append(company.split(".")[0])
    for target in targetList:
        if target not in companyList:
            print(target, "is missing")
            return False
    if 'data' not in os.listdir("."):
        os.mkdir("data")
    return True

def data_correction(last_year) -> list:
    return last_year

def read_all_companies(targetList) -> None:
    for target in targetList:
        file = open("stocks/"+target+".csv", "r")
        output_file = open("data/"+target+".csv", "w")
        lines = (file.read()).split("\n")
        last_year = lines[-255:]
        fixed_data = data_correction(last_year)
        for data in fixed_data:
            output_file.write(data+"\n")
        file.close()
        output_file.close()


#"NSRGY" "MA"
def main() -> None:
    targetList = ["NFLX", "GOOG", "AMZN", "MSFT", "FB", "GE", "CMCSA", "WFC", "MAR", "JPM"]
    if check_list_of_companies(targetList):
        read_all_companies(targetList)
        print("done!")
    else:
        print("missing")

if __name__ == "__main__":
    main()
