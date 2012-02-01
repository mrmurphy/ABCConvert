import threading
import sqlite3
class ShotDBInterface(threading.Thread):
    def __init__(self, dbname="shots.sqlite"):
        threading.Thread.__init__(self)
        #DB Stuff:
        self.dbname = dbname

    def OpenDB(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cur = self.conn.cursor()

    def CommitAndCloseDB(self):
        self.conn.commit()
        self.conn.close()

    def GetStatus(self, rowid):
        self.OpenDB()
        self.cur.execute("SELECT finished FROM Shots WHERE rowid=?",
                (rowid,))
        retstr = str(self.cur.fetchone()[0])
        self.CommitAndCloseDB()
        return retstr

    def GetLog(self, rowid):
        self.OpenDB()
        self.cur.execute("SELECT log FROM Shots WHERE rowid=?",
                (rowid,))
        retstr = str(self.cur.fetchone()[0])
        self.CommitAndCloseDB()
        return retstr
