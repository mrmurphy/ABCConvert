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
        self.log += "Just starting sleeping process. \n"
        time.sleep(1);
        self.log += "Just finishing sleeping process. \n"
        alert("Convert finished");
        self.finished = True;
