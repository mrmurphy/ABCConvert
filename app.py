## Append to path:
import sys
import os
sys.path.append("python/")
## Do imports:
from bottle import route, run, static_file, template
import sqlite3
#######################
# TODO: Make a CFG file?
db_name = "shots.sqlite"


@route('/app/<root>')
@route('/app/<root>/<path:path>')
def callback(root, path="/grp5/"):
    return template('templates/main.tpl', active=root, filepath=path)


@route('/RunConvert/<path:path>')
def callback(path):
    if not (os.path.exists(path)):
        return "ERROR: That file does not exist."
    import Shot
    curshot = Shot.Shot(path)
    curshot.run()
    return curshot.GetId()


@route('/GetDB/single/<column>/<id>')
def callback(column, id):
        entries = ExecQuery("""
        select %s from shots where rowid=%s
        """ % (column, id))
        return entries[0]


@route('/GetDB/history')
def GetDBHistory():
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("""
        select rowid,* from Shots
        """)
        entries = cur.fetchall()
        return template("templates/histlist.tpl", ent=entries)


@route('/GetDB/history/:id')
def GetDBHistoryByID(id=''):
        entries = ExecQuery("""
        select name,log,date,progress from shots where rowid=%s
        """ % (id))
        return template("templates/histdisp.tpl", ent=entries[0])


def ExecQuery(query):
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query)
        entries = cur.fetchall()
        return entries


@route('/static/<path:path>')
def callback(path):
    return static_file(path, root="")

run(host='localhost', port=8080, reloader=True, debug=True)
#run(host='ct75rf15', port=8080)
