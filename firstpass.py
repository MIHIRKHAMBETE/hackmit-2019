from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def choosePerson():
    return '''
    <a href='/responder'>First Responder</a><br>
    <a href='/patrienttriage'>Triage Patient</a><br><br>
    
    <a href='/commander'>IncidentCommander</a><br>
    <a href='/triage'>Add Patient</a><br><br>
    
    <a href='/dispatch'>Dispatch</a><br>
    '''


@app.route('/responder')
def responder():
    return render_template('responder.html')

@app.route('/triage')
def patrienttriage():
    return render_template('triage.html')

@app.route('/commander')
def commander():
    return '<h1>Incident Commander</h1>'


@app.route('/dispatch')
def dispatch():
    return '<h1>Dispatch</h1>'
