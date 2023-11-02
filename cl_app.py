from ProductionCode.stocks import Stocks
import sys 

def main(arguments):

    # TODO fix this to handle with database

    Stock = Stocks()
    #list of all company codes to be parsed
    data = {}


    if len(arguments) < 2:
        print("Bad input. Please type in --get_h to see your options!")
        return None

    match arguments[1]:
        case "--get_h":
            Stock.get_help()
        case "--get_by_company":
            data = Stock.get_by_company(arguments[2:])
        case "--get_by_date":
            data = Stock.get_by_date(arguments)
    Stock.print_data(data)

if __name__ == "__main__":
    main(sys.argv)