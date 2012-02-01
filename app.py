import sys
sys.path.append("python/")
from bottle import route, run, static_file
import Shot
import ShotDBInterface

curShot = Shot.Shot("default")
curSid = curShot.GetId()
sdb = ShotDBInterface.ShotDBInterface("shots.sqlite")

@route('/NewConvert/:name')
def NewShot(name=''):
    curShot.SetName(name)
    curShot.run()
    return '<b>Now converting %s!</b>' % name

@route('/CheckStatus')
def CheckStatus():
    """
    stats = sdb.GetStatus(curSid)
    return {'stats':stats}
    """
    return {'stats':"True"}

# For routing normal html
@route('/main')
def MainPage():
    htmllist = open("html/index.html", 'r').readlines()
    htmlstr = " ".join(htmllist)
    return htmlstr

@route('/images/:filename')
def GetImage(filename):
    return static_file(filename, root='images/')
@route('/javasc/:filename')
def GetJava(filename):
    return static_file(filename, root='javasc/')
@route('/styles/:filename')
def GetStyles(filename):
    return static_file(filename, root='styles/')

run(host='localhost', port=8080, reloader=True)
