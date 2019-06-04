import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/zagreb", methods=["GET"])
def zagreb():

    grad = "Zagreb"

    unit = "metric"

    apikey = "e998129b509f75e000cfc1898060cb46"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("Zagreb.html", data=data.json())

@app.route("/osijek", methods=["GET"])
def osijek():

    grad = "Osijek"

    unit = "metric"

    apikey = "e998129b509f75e000cfc1898060cb46"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("Osijek.html", data=data.json())

@app.route("/split", methods=["GET"])
def split():

    grad = "Split"

    unit = "metric"

    apikey = "e998129b509f75e000cfc1898060cb46"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("Split.html", data=data.json())



if __name__ == '__main__':
    app.run()
