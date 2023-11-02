import psycopg2
from ProductionCode.helper import * 

## fix later 
database = 'teamh'
user = 'teamh'
password = 'expo795phone'
portNumbers = '5120 5230'


class DataSource:

    def __init__(self):
        '''Constructor that initiates connection to database'''
        self.connection = self.connect()


    def connect(self):
        '''Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object.'''

        try:
            connection = psycopg2.connect(database=database, user=user, password=password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
    

    def fetch_data(self, companyTuple, dateTuple):
        ''' Arguments: takes in tuple of companies and tuple of dates based on user's form input 
        Purpose: Makes queries based on user's input of companies and dates
        Return: list of tuples with (company, date, value) ''' 

        cursor = self.connection.cursor()
        # fails if user doesn't supply anything
        if isEmpty(dateTuple): ## for if user doesn't input a date 
            cursor.execute("select * from allstockdata where company in %s", (companyTuple,))
        else:
            cursor.execute("select * from allstockdata where company in %s and date in %s", (companyTuple, dateTuple))
        fetchedData = cursor.fetchall()
        cursor.close()
        return fetchedData 