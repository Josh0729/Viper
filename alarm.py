import time

class Alarm(object):
    
    def __init__(self):
        self.disableAlarm()
        
    def setAlarm(self,timeToSet):
        self.alarmSet = True
        self.alarmTime = timeToSet
        
    def disableAlarm(self):
        self.alarmSet = False
        self.alarmTime = None
        self.reoccurring = False
        self.reoccurringDays = None
        self.reoccuringPattern = None
    
    def checkAlarm(self):
        if self.alarmSet == True:
            if self.alarmTime == time.strftime('%I:%M %p').lstrip('0'):
                self.disableAlarm() 