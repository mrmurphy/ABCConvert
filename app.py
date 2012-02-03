## Append to path:
import sys
sys.path.append("python/")
## Do imports:
from bottle import route, run, static_file, template
import Shot
#######################

shots = {}
CurShotId = 0
#curSid = curShot.GetId()

# For routing normal html
@route('/main')
def MainPage():
    return template('templates/main')

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
