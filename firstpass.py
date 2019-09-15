import requests
import datetime as dt
from datetime import timedelta
from flask import Flask, render_template, request, url_for, redirect

import mci
import ibm_get_test
app = Flask(__name__)

middle_url = "http://triageapp.appspot.com/data"
# assume for now there is only one mci to track
# this_mci = mci.MCI(dt.datetime.now(), "location",  "commander", [mci.Responder('MIT8')])

mcis = [mci.MCI(0, dt.datetime.now()-timedelta(hours=30),  "Apollo Theater",  "commander", {})] # test only
mcis[0].addResponders(['MIT8', 'P1', 'Squad2'])
# mcis = []
# this_mci = mci.MCI(dt.datetime.now(), 2, "Apollo Theater",  "Commander", {})
# this_mci = None


@app.route('/', methods=['GET', 'POST'])
def index():
    global mcis
    if request.method == "GET":
        return render_template('index.html', mcis=mcis)
    elif request.method == "POST":
        # Report Incident button pressed: initialize new mci!
        # global this_mci
        # this_mci = mci.MCI(len(mcis), dt.datetime.now(), "Apollo Theather",  "Commander", {})
        # for testing purposes, add more responders & patients
        this_mci.addResponders(['MIT8', 'P1', 'Squad2'])
        this_mci.addPatient('left side of lobby', 'R', 'Hemorrhage (tourniquet placed)')
        this_mci.addPatient('stairwell to right of lobby', 'Y')
        this_mci.addPatient('sidewalk next to bldg, leaning on pole', 'G')
        this_mci.addPatient('red couch by elevator', 'G')
        this_mci.addPatient('behind lobby staff counter', 'B', 'cardiac arrest')

        ic = request.form.get("ic")
        # if ic: return redirect(url_for("commander"))
        if ic: return redirect(url_for("commander")+"/" + str(ic))
        triage = request.form.get("triage")
        if triage: return redirect(url_for("triage")+"/" + str(triage))
        responder = request.form.get("responder")
        if responder: return redirect(url_for("responder")+"/" + str(responder))
        dispatch = request.form.get("dispatch")
        if dispatch: return redirect(url_for("dispatch")+"/" + str(dispatch))

        report = request.form.get("report")
        if report:
            print(report)
            i = len(mcis)
            this_mci = mci.MCI(i, dt.datetime.now(), "Bronx, NYC",  "commander", {})
            this_mci.addResponders(['MIT8', 'P1', 'Squad2'])
            mcis.append(this_mci)
            # return redirect(url_for(str(i))+"/commander")
            return redirect(url_for("commander")+"/" + str(i))
        # return redirect(url_for(str(i))+"/commander")

@app.route('/commander', defaults={'mcid': 0}, methods=['GET', 'POST'])
@app.route('/commander/<mcid>', methods=['GET', 'POST'])
def commander(mcid):
    if request.method == "POST":
        # global this_mci
        result = request.form["passignee"]
        pt, responder = result.split('~') #assumeing no responder id's will have ~ in their call sign
        mcis[int(mcid)].patientDict[int(pt)].reassign(responder)
        mcis[int(mcid)].responders[responder].reassign(pt)
        # maybe sort the patient list before passing!
        # unassigned on top
        # red -> yellow -> green -> black
    return render_template('commander.html', responders=mcis[int(mcid)].responders.values(), patients=mcis[int(mcid)].patientDict.values())

@app.route('/triage', defaults={'mcid': 0}, methods=['GET', 'POST'])
@app.route('/triage/<mcid>', methods=['GET', 'POST'])
def triage(mcid):
    if request.method == "GET":
        return render_template('triager.html', patients=mcis[int(mcid)].patientDict.values())
    elif request.method == "POST":
        #press the add patient button!
        return redirect(url_for("patientadd"))
        # return render_template('triager.html', patients=this_mci.patientDict.values())

@app.route('/patientadd', defaults={'mcid': 0}, methods=['GET', 'POST'])
@app.route('/patientadd/<mcid>', methods=['GET', 'POST'])
def patientadd(mcid):
    if request.method == "GET":
        return render_template('patientadd.html')
    elif request.method == "POST":
        ploc = request.form["ploc"]
        status = request.form["options"]
        pcond = request.form["pcond"]
        pneed = request.form["pneed"]
        mcis[int(mcid)].addPatient(ploc, status, pcond, pneed)
        return redirect(url_for("triage"))

@app.route('/responder', defaults={'mcid': 0, 'id': None}, methods=['GET', 'POST'])
@app.route('/responder/<mcid>',  defaults={'id': None}, methods=['GET', 'POST'])
@app.route('/responder/<mcid>/<id>',  methods=['GET', 'POST'])
def responder(mcid, id):
    if request.method == "GET":
        if id:
            patient=mcis[int(mcid)].patientDict[int(mcis[int(mcid)].responders[id].assignee)]
            params = ['longitude', 'latitude', 'odometer', 'fuel_level']
            vals = []
            for param in params:
                vals.append(requests.get(middle_url, {'param': param}).text)
            rainy = ibm_get_test.get_ibm_weather_at(vals[1], vals[0])['observation']['precip_hrly'] > 0
            return render_template('responder.html', responder=id, patient=patient, vals=vals, rainy=rainy)
        else: # id = None; go to list of responders w/ general info!
        #maybe populate w/ general info..
            return render_template('responderlist.html', responders=mcis[int(mcid)].responders.values())
    elif request.method == "POST":
        if id: # "patient cleared" button was pressed... do something?
            # refusal = request.form.get("refusal")
            # transport = request.form.get("transport")
            # transfer = request.form.get("transfer")
            # return (refusal, transport, transfer)
            # if refusal or transfer, clear the assignment from both
            # if transport, pull up a map??
            rid = request.form["options"]
            return redirect(url_for("responder")+"/"+mcid+"/"+rid)
        else: #first responder checkin!
            rid = request.form["options"]
            return redirect(url_for("responder")+"/"+mcid+"/"+rid)

@app.route('/dispatch', defaults={'mcid': 0}, methods=['GET', 'POST'])
@app.route('/dispatch/<mcid>',  methods=['GET', 'POST'])
def dispatch(mcid):
    if request.method == "GET":
        rainy = True
        return render_template('dispatch.html', rainy=True)
