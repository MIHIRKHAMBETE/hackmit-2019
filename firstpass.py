import requests
from flask import Flask, render_template, request
app = Flask(__name__)

middle_url = "http://triageapp.appspot.com/data"
pid = "pid"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/commander')
def commander():
    return render_template('commander.html')


@app.route('/triager')
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
        return request.form
