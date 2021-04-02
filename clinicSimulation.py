from DataStructures import Queue
from Doctors import Doctor
from patients import Patient
import random

def simulation(workingTime, patientPerMIn):
    clinicDoctor = Doctor(patientPerMIn)
    waitingHall = Queue()
    waitingTIme = []

    for currrentMin in range(workingTime):

        if random.randrange(1,7) == 6:  # A patient every 6 Minutes
            ThePatient = Patient(currrentMin)
            waitingHall.enqueue(ThePatient)

        if (not clinicDoctor.busy()) and (not waitingHall.isEmpty()):
            NextPatient = waitingHall.dequeue()
            waitingTIme.append(NextPatient.WaitingTime(currrentMin))
            clinicDoctor.startNewP(NextPatient)

        clinicDoctor.tick()

    AvgWait = sum(waitingTIme) / len(waitingTIme)
    print("Average Wait for",len(waitingTIme) ," patients is ",AvgWait, "Minuets", waitingHall.size(), "patient remaining")


for i in range(10):
    simulation(240, 5)