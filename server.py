from flask import Flask, render_template
from random import randint



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/random")
def random():
    numbers = [randint(1, 101) for i in range(10)]
    soucet_cisel = sum(numbers)
    return render_template("random.html", data=numbers, data2=soucet_cisel)


if __name__ == "__main__":
    app.run(debug=True)