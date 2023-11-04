from ProductionCode.stocks import Stocks
import sys 

def main(arguments):
    '''Purpose: Cl app with 3 features: print all stocks for a specific comapny, print stocks for a company on a specific date, or help users use the app.'''
    
    stock = Stocks()

    if len(arguments) < 2:
        print("Bad input. Please type in --get_h to see your options!")
        return None

    if arguments[1] == "--get_company":
        data = stock.get_data([arguments[2]], []) 
        print(data)
    elif arguments[1] == "--get_on_date":
        data = stock.get_data([arguments[2]], [arguments[3]]) 
        print(data)
    elif arguments[1] =="--get_h" or "--get_help":
        print(stock.get_help())


if __name__ == "__main__":
    main(sys.argv)