import requests
import datetime as dt
from flask import Flask, render_template, request, url_for, redirect

import mci
app = Flask(__name__)

middle_url = "http://triageapp.appspot.com/data"
pid = "pid"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        # Report Incident button pressed: initialize new mci!
        responders = []
        this_mci = mci.MCI(dt.datetime.now(), "location",  "commander", responders)
        return redirect(url_for("commander"))


@app.route('/commander')
def commander():
    return render_template('commander.html')


@app.route('/triage')
def triager():
    return render_template('triager.html')


@app.route('/patientadd', methods=['GET', 'POST'])
def patientadd():
    if request.method == "GET":
        return render_template('patientadd.html')
    elif request.method == "POST":
        return request.form

@app.route('/responder')
def responder():
    if request.method == "GET":
        params = ['longitude', 'latitude', 'odometer', 'fuel_level']
        vals = []
        for param in params:
            vals.append(requests.get(middle_url, {'param': param}).text)
        return render_template('responder.html', vals=vals)
    elif request.method == "POST":
        # "patient cleared" button was pressed... do something?
        return request.form
