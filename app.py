import sys
sys.path.append("python/")
from bottle import route, run, static_file
import Shot

shots = {}
CurShotId = 0
#curSid = curShot.GetId()

@route('/NewConvert/:name')
def NewShot(name=''):
    global shots
    global CurShotId
    curShot = Shot.Shot(name)
    CurShotId = curShot.GetId()
    shots[CurShotId] = curShot
    curShot.run()
    return '<b>Now converting %s!</b>' % name

@route('/CheckShot')
def CheckShot():
    global shots
    global CurShotId
    print "I'm in checkshot"
    finished = shots[CurShotId].GetFinished()
    log = shots[CurShotId].GetLog()
    return {'finished':finished, 'log':log}

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
