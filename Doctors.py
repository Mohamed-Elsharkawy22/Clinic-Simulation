
class Doctor:
    def __init__(self, examinationRatio):
        self.patientPerMin = examinationRatio
        self.currentPatient = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentPatient is not None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentPatient = None

    def busy(self):
        if self.currentPatient is not None:
            return True
        else:
            return False

    def startNewP(self, newPatient):
        self.currentPatient = newPatient
        self.timeRemaining = newPatient.getAge() / self.patientPerMin

