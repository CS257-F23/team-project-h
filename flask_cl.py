from flask import Flask, render_template
from ProductionCode.stock_data import *

app = Flask(__name__)

def isEmpty(data):
    if len(data) == 0:
        return True
    return False

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/get_help")
def get_help():
    return render_template('help.html')

@app.route("/get_company/<companyList>")
def get_company(companyList):
    allCompaniesData = load()
    data = get_by_company(allCompaniesData, companyList.split(","))
    if isEmpty(data):
        return render_template("error.html")
    return render_template('display.html', companyData = data)

@app.route("/get_date/<dateList>")
def get_date(dateList):
    allCompaniesData = load()
    data = get_by_date(allCompaniesData, dateList.split(","))
    if isEmpty(data):
        return render_template("error.html")
    return render_template('display.html', companyData = data)


@app.errorhandler(404)
def not_found(e):
    return render_template('error.html')

@app.errorhandler(500)
def bug(e):
    return render_template('error.html')

if __name__ == "__main__":
    app.run()