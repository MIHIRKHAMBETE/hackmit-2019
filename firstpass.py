from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def choosePerson():
    return '''
    <a href='/commander'>IncidentCommander</a><br><br>
    
    <a href='/triager'>Triager</a><br>
    <a href='/patientadd'>Add Patient</a><br><br>
    
    <a href='/responder'>First Responder</a><br>
    '''


@app.route('/commander')
def commander():
    return '<h1>Incident Commander</h1>'


@app.route('/triager')
def triager():
    return '<h1>Triager</h1>'


@app.route('/patientadd')
def patientadd():
    return render_template('patientadd.html')

@app.route('/responder')
def responder():
    return render_template('responder.html')
