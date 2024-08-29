from flask import Flask
import random
from random import randint


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

@app.route("/random/<count>")
def random_page(count):
    output = "Loteria: "
    for i in range(int(count)):
        output += f" {randint(1, 100)}, "

    return output


@app.route("/random2/<int:count>")
def random_page2(count):
    output = "Loteria: "
    for i in range(count):
        output = f" {randint(1, 100)}, "

    return output

@app.route("/soucet/<int:count>")
def soucet(count):
    nahodna_cisla = [random.randint(1, 101) for _ in range(count)]
    soucet_cisel = sum(nahodna_cisla)
    output = "Čísla: " + ", ".join(str(cislo) for cislo in nahodna_cisla)
    output += (f" <br> Celkový součet: {soucet_cisel}")
    return output

if __name__ == "__main__":
    app.run(debug=False)

