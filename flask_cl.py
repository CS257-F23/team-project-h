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
        companies = []
        dates = []
        for inp in userIn:
            if "company" in inp:
                companies.append(userIn[inp])
            else:
                dates = userIn[inp].split(",")
                if "" in dates:
                    dates.remove("")
        displayData = Stock.get_by_company(companies)
        if len(dates) >= 1:
            displayData = Stock.get_by_date(dates, displayData)
        if len(companies) >= 1:
            return render_template("research.html", companyData = displayData, company=companies[0])
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
    app.run(debug=True)
