import psycopg2
from ProductionCode.helper import * 
from ProductionCode.psqlConfig import *

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
        Purpose: Fetch data from queries based on user's input 
        Return: list of tuples with (company, date, value) ''' 
        if isEmpty(dateTuple): 
            return self.fetch_only_companies(companyTuple)
        else:
            return self.fetch_companies_and_dates(companyTuple, dateTuple)

    def fetch_only_companies(self, companyTuple):
        '''Arguments: takes in a tuple of companies 
        Purpose: Executes a query for companies in the tuple. 
        Return: list of tuples with data from the query '''
        cursor = self.connection.cursor()
        cursor.execute("select * from allstockdata where company in %s", (companyTuple,))
        fetchedData = cursor.fetchall()
        cursor.close()
        return fetchedData
    
    def fetch_companies_and_dates(self, companyTuple, dateTuple):
        '''Arguments: takes in tuples of companies and of dates
        Purpose: Executes a query for companies in the tuple. 
        Return: list of tuples with data from the query '''
        cursor = self.connection.cursor()
        cursor.execute("select * from allstockdata where company in %s and date in %s", (companyTuple, dateTuple))
        fetchedData = cursor.fetchall()
        cursor.close()
        return fetchedData
    