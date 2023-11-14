from ProductionCode.stocks import *

class Predict():

    def predict(self, userIn):
            '''Purpose: This function predicts how much the stocks will earn/lose based on user investment.
            Args:
                userIn (dict): User investment input
            Returns:
                tuple: returns the initial investment amount, final investment amount, and the difference.
            '''

            data = Stocks()
            alldata = data.get_all_data()
            initial, final = 0.0, 0.0 
            if userIn == None:
                return None
            try:
                for companyValue in userIn:
        
                    initial += float(userIn[companyValue])
                    factor = float(alldata[companyValue]["2020-04-01"] / alldata[companyValue]["2019-04-01"]) ## calculates slope of the stock 
                    final += float(userIn[companyValue]) * factor
            except:
                pass
            final = round(final, 2)
            return (initial, final, round(final-initial, 2)) 