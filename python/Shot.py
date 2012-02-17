import time
import datetime
import sqlite3
import multiprocessing as mproc

class Shot():
    def __init__(self, shotName, dbname="shots.sqlite"):
        self.shotName = shotName
        self.dbname = dbname
        date = str(datetime.datetime.now())
        self.OpenDB()
        self.cur.execute("INSERT INTO Shots (name, finished, date, \
            user, progress) VALUES (?,?,?,?,?)", \
            (shotName, 'False', date, 'default', '0'))
        self.rowid = str(self.cur.lastrowid)
        self.conn.commit()
        self.CommitAndCloseDB()

    ################
    ###### Public Methods ######
    def run(self):
        p = mproc.Process(target=self._processShot)
        p.start()
    ######


    ############
    ##### Private Member Methods ######
    def _processShot(self):
        self.UpdateLog("Just starting to sleep...")
        time.sleep(5)
        self.UpdateLog("I'm still sleeping")
        self.UpdateProgress("25")
        time.sleep(3)
        self.UpdateLog("Yep, no joke")
        self.UpdateProgress("50")
        time.sleep(2)
        self.UpdateLog("Am I close?")
        self.UpdateProgress("75")
        time.sleep(2)
        self.UpdateLog("Just finished sleeping.")
        self.UpdateProgress("100")
        self.UpdateFinished("True")
    ############

########################################
#################### Database Section
########################################

    def UpdateFinished(self, status):
        self.OpenDB()
        self.cur.execute("UPDATE Shots SET finished = ? where rowid = ?",
                (status, self.rowid))
        self.CommitAndCloseDB()

    def OpenDB(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cur = self.conn.cursor()

    def CommitAndCloseDB(self):
        self.conn.commit()
        self.conn.close()

    def UpdateLog(self, message):
        self.OpenDB()
        self.cur.execute("SELECT log FROM Shots WHERE rowid=?",
                (self.rowid,))
        orig = str(self.cur.fetchone()[0])
        if (orig != "None"):
            message = orig + "<br>" + message
        self.cur.execute("UPDATE Shots SET log = ? where rowid = ?",
                (message, self.rowid))
        self.CommitAndCloseDB()
    
    def UpdateProgress(self, prog):
        self.OpenDB()
        self.cur.execute("UPDATE Shots SET progress = ? WHERE rowid=?",
                (prog, self.rowid))
        self.CommitAndCloseDB();

    def SetName(self, name):
        self.OpenDB()
        self.cur.execute("UPDATE Shots SET name = ? where rowid = ?",
                (name, self.rowid))
        self.CommitAndCloseDB()

    def GetId(self):
        return self.rowid

    def GetFinished(self):
        self.OpenDB()
        self.cur.execute("SELECT finished FROM Shots WHERE rowid=?",
                (self.rowid,))
        retstr = str(self.cur.fetchone()[0])
        self.CommitAndCloseDB()
        return retstr

    def GetLog(self):
        self.OpenDB()
        self.cur.execute("SELECT log FROM Shots WHERE rowid=?",
                (self.rowid,))
        retstr = str(self.cur.fetchone()[0])
        self.CommitAndCloseDB()
        return retstr

########################################
########################################
