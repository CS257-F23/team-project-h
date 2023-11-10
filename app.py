from flask import Flask, render_template, request, redirect
from ProductionCode.stocks import *
from ProductionCode.helper import *

app = Flask(__name__)

stock = Stocks()
companyList = ["AMZN", "CMCSA", "FB", "GE", "GOOG" ,"JPM", "MAR", "MSFT", "NFLX", "WFC"]


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
        userInput = request.form
        inputList = parse_user_input(userInput)
        companies, dates = inputList[0], inputList[1]

        displayData = stock.get_data(companies, dates)
        if not isEmpty(companies):
            return render_template("research.html", companyList=companyList, companyData = displayData, company=companies[0])
    return render_template('research.html', companyList=companyList)


def parse_user_input(userInput):
    '''Parses user input for companies and dates. 
    Argument: User input (dictionary)
    Returns: List of 2 lists [[companies, dates]'''
    inputList, companies, dates = [], [], []
    for key in userInput:
        if "date" not in key:
            companies.append(userInput[key])
        else:
            dates = userInput[key].split(",")
            if "" in dates:
                dates.remove("")
    inputList.append(companies)
    inputList.append(dates)
    return inputList

@app.route("/play", methods=("GET", "POST"))
def play():
    '''Play page that predicts investment gains based on the user's input. The route takes HTTP methods.
       User will input a value for investments for each company in the form. '''
    if request.method == "POST":
        userIn = request.form
        values = stock.predict(userIn)
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
    app.run(port=5108)
