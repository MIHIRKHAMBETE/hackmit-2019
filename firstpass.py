import requests
import datetime as dt
from flask import Flask, render_template, request, url_for, redirect

import mci
app = Flask(__name__)

middle_url = "http://triageapp.appspot.com/data"
# assume for now there is only one mci to track
# this_mci = mci.MCI(dt.datetime.now(), "location",  "commander", [mci.Responder('MIT8')])
mcis = [mci.MCI(dt.datetime.now(), "Apollo Theater",  "Commander", {})] # test only
this_mci = None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html', mcis=mcis)
    elif request.method == "POST":
        # Report Incident button pressed: initialize new mci!
        global this_mci

        this_mci = mci.MCI(dt.datetime.now(), "Apollo Theather",  "Commander", {})
        # for testing purposes, add more responders & patients
        this_mci.addResponders(['MIT8', 'P1', 'Squad2'])
        this_mci.addPatient('left side of lobby', 'R', 'Hemorrhage (tourniquet placed)')
        this_mci.addPatient('stairwell to right of lobby', 'Y')
        this_mci.addPatient('sidewalk next to bldg, leaning on pole', 'G')
        this_mci.addPatient('red couch by elevator', 'G')
        this_mci.addPatient('behind lobby staff counter', 'B', 'cardiac arrest')
        # for pt in this_mci.patientDict.keys():
        #     this_mci.patientDict[pt].reassign('P1')
        return redirect(url_for("commander"))


@app.route('/commander', methods=['GET', 'POST'])
def commander():
    if request.method == "POST":
        global this_mci
        result = request.form["passignee"]
        pt, responder = result.split('~') #assumeing no responder id's will have ~ in their call sign
        this_mci.patientDict[int(pt)].reassign(responder)
        this_mci.responders[responder].reassign(pt)
        # maybe sort the patient list before passing!
        # unassigned on top
        # red -> yellow -> green -> black
    return render_template('commander.html', responders=this_mci.responders.values(), patients=this_mci.patientDict.values())

@app.route('/triage', methods=['GET', 'POST'])
def triage():
    if request.method == "GET":
        return render_template('triager.html', patients=this_mci.patientDict.values())
    elif request.method == "POST":
        #press the add patient button!
        return redirect(url_for("patientadd"))
        # return render_template('triager.html', patients=this_mci.patientDict.values())


@app.route('/patientadd', methods=['GET', 'POST'])
def patientadd():
    if request.method == "GET":
        return render_template('patientadd.html')
    elif request.method == "POST":
        return redirect(url_for("triage"))

@app.route('/responder', defaults={'id': None}, methods=['GET', 'POST'])
@app.route('/responder/<id>',  methods=['GET', 'POST'])
def responder(id):
    if request.method == "GET":
        if id:
            patient=this_mci.patientDict[int(this_mci.responders[id].assignee)]
            params = ['longitude', 'latitude', 'odometer', 'fuel_level']
            vals = []
            for param in params:
                vals.append(requests.get(middle_url, {'param': param}).text)
            return render_template('responder.html', responder=id, patient=patient, vals=vals)
        else: # id = None; go to list of responders w/ general info!
        #maybe populate w/ general info..
            return render_template('responderlist.html', responders=this_mci.responders.values())
    elif request.method == "POST":
        if id: # "patient cleared" button was pressed... do something?
            # refusal = request.form.get("refusal")
            # transport = request.form.get("transport")
            # transfer = request.form.get("transfer")
            # return (refusal, transport, transfer)
            # if refusal or transfer, clear the assignment from both
            # if transport, pull up a map??
            pass
        else: #first responder checkin!
            rid = request.form["options"]
            return redirect(url_for("responder")+"/"+rid)
