import random


class patient():

    def __init__(self, id, location, triage, condition, need):
        id = id
        location = location
        triage = triage
        condition = condition
        need = need
        assignment = None
    
    def reassign(self, person)
        self.assignment = person

class mci():

    def __init__(self, date, time, location, ic):
        date = date
        time = time
        location = location
        ic = ic
        patients = []
    
    def addPatient(self, location, triage, condition, need):
        pid = random.randint(1000, 9999)
        self.patients.append([patient(pid)])