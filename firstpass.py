import requests
import datetime as dt
from flask import Flask, render_template, request, url_for, redirect

import mci
app = Flask(__name__)

middle_url = "http://triageapp.appspot.com/data"
# assume for now there is only one mci to track
# this_mci = mci.MCI(dt.datetime.now(), "location",  "commander", [mci.Responder('MIT8')])
this_mci = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        # Report Incident button pressed: initialize new mci!
        global this_mci

        this_mci = mci.MCI(dt.datetime.now(), "location",  "commander", [])
        # for testing purposes, add more responders & patients
        this_mci.addResponders(['MIT8', 'P1', 'Squad2'])
        this_mci.addPatient('left side of lobby', 'R', 'Hemorrhage (tourniquet placed)')
        this_mci.addPatient('stairwell to right of lobby', 'Y')
        this_mci.addPatient('sidewalk next to bldg, leaning on pole', 'G')
        this_mci.addPatient('red couch by elevator', 'G')
        this_mci.addPatient('behind lobby staff counter', 'B', 'cardiac arrest')
        return redirect(url_for("commander"))


@app.route('/commander', methods=['GET', 'POST'])
def commander():
    if request.method == "POST":
        print(request.form)
        # respIDs = []
        # for responder in this_mci.responders:
        #     respIDs.append(responder.id)

    return render_template('commander.html', responders=this_mci.responders, patients=this_mci.patientDict.values())

@app.route('/triage', methods=['GET', 'POST'])
def triager():
    if request.method == "GET":
        return render_template('triager.html')
    elif request.method == "POST":
        return render_template('triager.html')


@app.route('/patientadd', methods=['GET', 'POST'])
def patientadd():
    if request.method == "GET":
        return render_template('patientadd.html')
    elif request.method == "POST":
        return request.form

@app.route('/responder', methods=['GET', 'POST'])
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
