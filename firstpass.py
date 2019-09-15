from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/commander')
def commander():
    return render_template('commander.html')


@app.route('/triager')
def triager():
    return render_template('triager.html')


@app.route('/patientadd')
def patientadd():
    return render_template('patientadd.html')

@app.route('/responder')
def responder():
    return render_template('responder.html')
