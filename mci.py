import random


class Patient:

    def __init__(self, location, status, condition, need):
        self.location = location
        self.status = status
        self.condition = condition
        self.need = need
        self.respondent = None
        self.cleared = False
    
    def reassign(self, respondent):
        self.respondent = respondent

    def changeStatus(self, status):
        self.status = status


class Dispatcher:

    def __init__(self):
        self.assignee = None

    def reassign(self, patientID):
        self.assignee = patientID


class MCI:

    def __init__(self, date, time, location, commander, dispatchers):
        self.date = date
        self.time = time
        self.location = location
        self.commander = commander
        self.patientDict = {}
        self.patientDone = []
        self.dispatchers = dispatchers
        self.incidence = True

    def assignPatient(self, dispatcherID, patientID):
        self.dispatchers[dispatcherID].reassign(patientID)
        self.patientDict[patientID].reassign(dispatcherID)
    
    def addPatient(self, location, triage, condition, need):
        pid = random.randint(1000, 9999)
        while pid in self.patientDict:
            pid = random.randint(1000, 9999)
        patient = Patient(location, triage, condition, need)
        self.patientDict[pid] = patient

    def changePatientStatus(self, dispatcherID, patientID, status):
        self.patientDict[patientID].changeStatus(status)
        if status == 'Refused' or status == 'Transported':
            self.patientDone.append(self.patientDict[patientID])
            del self.patientDict[patientID]
        if len(self.patientDict) == 0:
            self.incidence = False