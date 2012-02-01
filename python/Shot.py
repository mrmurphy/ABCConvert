import time
import threading
import sqlite3

class Shot(threading.Thread):
    def __init__(self, shotName, dbname="shots.sqlite"):
        self.shotName = shotName
        threading.Thread.__init__(self)
        #DB Stuff:
        self.dbname = dbname
        self.OpenDB()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Shots (name TEXT, \
                log TEXT, finished TEXT)''')
        self.cur.execute("INSERT INTO Shots (name, finished) VALUES \
                (?,'False')", (shotName,))
        self.rowid = str(self.cur.lastrowid)
        self.conn.commit()
        self.CommitAndCloseDB()

    def run(self):
        self.UpdateLog("Just starting to sleep...")
        time.sleep(5)
        self.UpdateLog("Just finished sleeping.")
        self.UpdateFinished("True")

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

    def SetName(self, name):
        self.OpenDB()
        self.cur.execute("UPDATE Shots SET name = ? where rowid = ?",
                (name, self.rowid))
        self.CommitAndCloseDB()

    def GetId(self):
        return self.rowid

    def GetStatus(self):
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
