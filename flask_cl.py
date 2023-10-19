from flask import Flask, render_template, request, redirect
from ProductionCode.cl import *

app = Flask(__name__)

Stock = Stocks()

def isEmpty(data):
    if len(data) == 0:
        return True
    return False

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/get_help")
def get_help():
    return render_template('help.html')

@app.route("/research", methods=("GET", "POST"))
def research():
    if request.method == "POST":
        userIn = request.form
        userCompany = []
        for company in userIn:
            if len(userIn[company]) <= 5:
                userCompany.append(userIn[company])
            else: #to add in dates
                pass
        displayData = Stock.get_by_company(userCompany)
        return render_template("research.html", companyData = displayData)
    return render_template('research.html')

@app.route("/get_date/<dateList>")
def get_date(dateList):
    data = Stock.get_by_date(dateList.split(","))
    if isEmpty(data):
        return render_template("error.html")
    return render_template('research.html', companyData = data)


@app.errorhandler(404)
def not_found(e):
    return render_template('error.html')

@app.errorhandler(500)
def bug(e):
    return render_template('error.html')

if __name__ == "__main__":
    app.run()