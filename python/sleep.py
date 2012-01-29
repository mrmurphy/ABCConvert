## A Small python script to test working with Apccelerator.
import time
import threading

class Shot(threading.Thread):
    def __init__(self, shotName):
        self.shotName = shotName
        self.finished = False
        self.log = ""
        threading.Thread.__init__(self)
        
    def GetLog(self):
        return self.log
    
    def GetStatus(self):
        return finished
    
    def run(self):
        self.log = "Just starting sleeping process."
        Titanium.API.runOnMainThreadAsync(writeOut, self.log)
        time.sleep(3);
        self.log = "Just finishing sleeping process."
        Titanium.API.runOnMainThreadAsync(writeOut, self.log)
        self.finished = True;

    def UpdateLog(self, message):
        self.log += message
        
