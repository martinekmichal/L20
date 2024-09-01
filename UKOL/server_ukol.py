from flask import Flask, render_template
from random import randint
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/time")
def time():
    aktualni_cas = datetime.now()
    aktualni_P = pytz.timezone("Europe/Prague")
    aktualni_L = pytz.timezone("Europe/London")
    aktualni_M = pytz.timezone("Europe/Moscow")
    aktualni_T = pytz.timezone("Asia/Tokyo")
    aktualni_NY = pytz.timezone("America/New_York")

    aktualni_praha = datetime.now(aktualni_P).strftime("%H:%M:%S")
    aktualni_Londyn = datetime.now(aktualni_L).strftime("%H:%M:%S")
    aktualni_Moskva = datetime.now(aktualni_M).strftime("%H:%M:%S")
    aktualni_Tokyo = datetime.now(aktualni_T).strftime("%H:%M:%S")
    aktualni_New_York = datetime.now(aktualni_NY).strftime("%H:%M:%S")


    return render_template("time.html",data=aktualni_praha, data1=aktualni_Londyn, data2=aktualni_Moskva, data3=aktualni_Tokyo, data4=aktualni_New_York)

if __name__ == "__main__":
    app.run(debug=True)