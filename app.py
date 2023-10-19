import ProductionCode as cl
from flask import Flask, render_template, request

app = Flask(__name__)




# data setup
labels = []
values = []
for row in data:
    labels.append(row[0])
    values.append(row[1])

# data setup
dataDict = {}
for key, value in zip(labels, values):
    dataDict[key] = value


def add_input_values(input):
    input_list = []

    for value in input:
        input_list.append(value)

    return input_list


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/play', methods=["GET", "POST"])
def play_page():
    """Displays a graph of the company data selected"""
    if request.method == "POST":
        company = request.form.values()
        form = add_input_values(company)
        if 'NFLX' in form:
            return render_template("play.html", form=form, labels=labels, values=values)

    return render_template('play.html')


@app.route('/research', methods=["GET", "POST"])
def research_page():
    """Displays a table page where user can get comapny data"""
    if request.method == "POST":
        company = request.form.values()
        form = add_input_values(company)
        if 'NFLX' in form:
            return render_template("research.html", form=form, dataDict=dataDict)

    return render_template("research.html",)


@app.route('/help')
def help_page():
    """Displays information about using the site"""
    return render_template("help.html")


@app.errorhandler(404)
def page_not_found(e):
    """Displays not found messages when route not found"""
    not_found_msg = "Sorry invalid page, please go back to the homepage."
    return not_found_msg


@app.errorhandler(500)
def python_bug(e):
    error_msg = "Sorry, there was an error try again."
    return error_msg


if __name__ == '__main__':
    app.run(port=1111)
