import psycopg2

from ProductionCode.config import config as config

class DataSource:

    def __init__(self):
        '''Constructor that initiates connection to database'''
        self.connection = self.connect()

    def connect(self):
        '''Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object.'''

        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
    
    def get_data(self, companyList, dateList):
        cursor = self.connection.cursor()
        if dateList.isEmpty():
            cursor.execute("select * from stockdata where company in %s", (companyList,))
        elif companyList.isEmpty():
            cursor.execute("select * from stockdata where date in %s", (dateList,))
        else:
            cursor.execute("select * from stockdata where company in %s and date in %s", (companyList, dateList))
        peepeepoopoo = cursor.fetchall()
        cursor.close()
        return peepeepoopoo

def main():
    shitfuck = DataSource()
    print(shitfuck.get_data(("AMZN", "GOOG"), ("2020-04-01", "2019-04-01")))

if __name__ == "__main__":
    main()