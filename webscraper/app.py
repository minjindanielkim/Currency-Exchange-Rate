import os
from flask import Flask
from flask import render_template
import scraper
import stock

app = Flask(__name__)

rates = scraper.exchange()

stocks = stock.indicies()


@app.route("/")
def index():
    return render_template("index.html", rates=rates)

@app.route("/stock")
def stock():
    return render_template("stock.html", stocks = stocks)
