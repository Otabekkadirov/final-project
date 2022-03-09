from datetime import date
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

    

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get input from the user
        name = request.form.get("name")
        birthday = request.form.get("birthday")

        # Validate the input
        if is_valid(name, birthday):
            days = calculate_days(birthday)
            weeks = calculate_weeks(birthday)
            return render_template("index.html", days=days, weeks=weeks)
            # return redirect("/")
        else:
            return render_template("error.html", message="Invalid input")
    elif request.method == "GET":
        return render_template("index.html")

    # # Get input from the user
    # name = request.args.get("name")
    # birthday = request.args.get("birthday")

    # # Validate the input
    # if is_valid(name, birthday):
    #     days = calculate_days(birthday)
    #     return redirect("index.html", days=days)
    # else:
    #     return render_template("error.html", message="Invalid input")

    # return render_template("index.html")





def is_valid(name, birthdate):
    if not name or not birthdate:
        return False
    return True


def calculate_days(birthdate):
    # Split the date string into integer
    x = birthdate.split("-")
    datelist = [int(i) for i in x]
    first_date = date(datelist[0], datelist[1], datelist[2])
    second_date = date.today()
    delta = second_date - first_date
    # print(delta.days)
    # print(type(second_date - first_date))
    return delta.days


def calculate_weeks(birthdate):
    days = calculate_days(birthdate)
    weeks = int(days / 7)
    return weeks