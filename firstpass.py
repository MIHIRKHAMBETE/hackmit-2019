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
    pid = 5551
    return render_template('patientadd.html')


@app.route('/responder')
def responder():
    pid = 6123
    loc = 'corner'
    pstatus = 'R'
    pcond = None
    return render_template('responder.html', pid=pid, loc=loc, pstatus=pstatus, pcond=pcond)
