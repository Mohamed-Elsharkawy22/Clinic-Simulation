import random


class Patient:
    def __init__(self, time):
        self.arrivalTime = time
        self.age = random.randrange(20, 61)

    def getAge(self):
        return self.age

    def WaitingTime(self, timeNow):
        return timeNow - self.arrivalTime
