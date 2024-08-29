from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home():
    return "Nazdar světe"



@app.route("/about")
def about():
    return "Okolo sekce "

@app.route("/cisla")
def cisla():
    nahodna_cisla = random.sample(range(1, 101), 3)
    return nahodna_cisla

if __name__ == "__main__":
    app.run(debug=False)

