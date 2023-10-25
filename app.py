from flask import Flask, render_template, request, redirect
from ProductionCode.cl import *

app = Flask(__name__)

Stock = Stocks()
companyList = ["AMZN", "CMCSA", "FB", "GE", "GOOG" ,"JPM", "MAR", "MSFT", "NFLX", "WFC"]

def isEmpty(data):
    '''Checks if the data is empty. 
    It takes in data as a dictionary. '''
    if len(data) == 0:
        return True
    return False

@app.route("/")
def homepage():
    '''Route for the homepage.
       It takes no arguments. '''
    return render_template('index.html')

@app.route("/help")
def help():
    '''Route for the help page.
       It takes no arguments. '''
    return render_template('help.html')

@app.route("/research", methods=("GET", "POST"))
def research():
    '''Research page that displays stock data based on user's input in the form.
       User will select companies in the form and input a date.'''
    if request.method == "POST":
        userIn = request.form
        companies = []
        dates = []
        for inp in userIn:
            if "date" not in inp:
                companies.append(userIn[inp])
            else:
                dates = userIn[inp].split(",")
                if "" in dates:
                    dates.remove("")
        displayData = Stock.get_by_company(companies)
        if len(dates) >= 1:
            displayData = Stock.get_by_date(dates, displayData)
        if len(companies) >= 1:
            return render_template("research.html", companyList=companyList, companyData = displayData, company=companies[0])
    return render_template('research.html', companyList=companyList)

@app.route("/play", methods=("GET", "POST"))
def play():
    '''Play page that predicts investment gains based on the user's input. The route takes HTTP methods.
       User will input a value for investments for each company in the form. '''
    if request.method == "POST":
        userIn = request.form
        values = Stock.predict(userIn)
        return render_template("play.html", companyList=companyList, start=values[0], end=values[1], difference=values[2])
    return render_template('play.html', companyList=companyList)


@app.errorhandler(404)
def not_found(e):
    '''404 Error page. 
       It takes in an error. '''
    return render_template('404.html')

@app.errorhandler(500)
def bug(e):
    '''500 Error page.
       It takes in an error. '''
    return render_template('500.html')

if __name__ == "__main__":
    app.run(debug=True)
