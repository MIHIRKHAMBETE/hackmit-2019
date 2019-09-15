import random


class Patient:

    def __init__(self, pid, location, status, condition, need):
        self.id = pid
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

    def __init__(self, did):
        self.id = did
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

    def addPatient(self, location, triage, condition, need):
        pid = random.randint(1000, 9999)
        while pid in self.patientDict:
            pid = random.randint(1000, 9999)
        patient = Patient(pid, location, triage, condition, need)
        self.patientDict[pid] = patient

    def assignPatient(self, dispatcherID):
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
        self.dispatchers[dispatcherID].reassign(patientID)
        self.patientDict[patientID].reassign(dispatcherID)

    def changePatientStatus(self, dispatcherID, patientID, status):
        self.patientDict[patientID].changeStatus(status)
        if status == 'Refused' or status == 'Transported':
            self.patientDone.append(self.patientDict[patientID])
            del self.patientDict[patientID]
            self.assignPatient(dispatcherID)
        if len(self.patientDict) == 0:
            self.incidence = False
