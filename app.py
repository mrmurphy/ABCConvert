## Append to path:
import sys
sys.path.append("python/")
## Do imports:
from bottle import route, run, static_file, template, view
import Shot
import sqlite3
#######################
# TODO: Make a CFG file?
db_name = "shots.sqlite"

# For routing normal html
@route('/main')
@route('/main/:page')
def MainPage(page=''):
    return template('templates/main.tpl', target=page)

@route('/convert/<path:path>')
def callback(path):
    args = {'active':'convert', 'filepath':path}
    return template('templates/main.tpl', active='convert', filepath=path)

@route('/history/')
def callback():
    return template('templates/history.tpl')

@route('/settings/')
def callback():
    return template('templates/settings.tpl')

@route('/GetStage/:name')
def GetStage(name=''):
    return template('templates/'+name)

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
        select name,log from Shots where rowid=%s
        """%(id))
        return template("templates/histdisp.tpl", ent=entries[0])

def ExecQuery(query):
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query)
        entries = cur.fetchall()
        return entries

@route('/images/:filename')
def GetImage(filename):
    return static_file(filename, root='images/')
@route('/javasc/:filename')
def GetJava(filename):
    return static_file(filename, root='javasc/')
@route('/styles/:filename')
def GetStyles(filename):
    return static_file(filename, root='styles/')

run(host='localhost', port=8080, reloader=True, debug=True)
