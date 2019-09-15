import random


class Patient:

    def __init__(self, pid, location, status, condition, need):
        self.id = pid
        self.location = location
        self.status = status
        self.condition = condition
        self.need = need
        self.responder = None
        self.cleared = False

    def reassign(self, responder): # just the id, not the object
        self.responder = responder

    def changeStatus(self, status):
        self.status = status


class Responder:

    def __init__(self, id):
        self.id = id # unique call sign
        self.assignee = None

    def reassign(self, patientID):
        self.assignee = patientID


class MCI:

    def __init__(self, datetime, location, commander, responders):
        self.datetime = datetime
        self.location = location
        self.commander = commander
        self.patientDict = {}
        self.patientDone = []
        self.responders = responders # dict, id = self.id
        self.incidence = True

    def addPatient(self, location, triage, condition='unknown', need='n/a'):
        pid = random.randint(1000, 9999)
        while pid in self.patientDict:
            pid = random.randint(1000, 9999)
        patient = Patient(pid, location, triage, condition, need)
        self.patientDict[pid] = patient

    def assignPatient(self, responderID):
        r = None
        y = None
        g = None
        for patientID in self.patientDict:
            if self.patientDict[patientID].status == 'R' and not r:
                r = patientID
            if self.patientDict[patientID].status == 'Y' and not y:
                y = patientID
            if self.patientDict[patientID].status == 'G' and not g:
                g = patientID
        if r:
            patientID = r
        elif y:
            patientID = y
        else:
            patientID = g
        self.responders[responderID].reassign(patientID)
        self.patientDict[patientID].reassign(responderID)

    def changePatientStatus(self, responderID, patientID, status):
        self.patientDict[patientID].changeStatus(status)
        if status == 'Refused' or status == 'Transported':
            self.patientDone.append(self.patientDict[patientID])
            del self.patientDict[patientID]
            self.assignPatient(responderID)
        if len(self.patientDict) == 0:
            self.incidence = False

    def addResponder(self, responderID):
        self.responders[responderID]= Responder(responderID)

    def addResponders(self, responderIDs):
        for rid in responderIDs:
            self.addResponder(rid)
