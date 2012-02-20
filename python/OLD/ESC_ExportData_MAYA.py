########## Configuration variables #############
liblocation = "/grp5/estefan/tools/converter/lib/"
loglevel = 'INFO'
loglocation = '/grp5/estefan/logs/conversions.log'
################################################

# Set up the logger:
import logging
log = logging.getLogger('log')
log.setLevel(getattr(logging, loglevel))
handler = logging.FileHandler(loglocation)
formatter = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

# Custom modules
log.info("Importing packages, and loading plugins...")

# Imports
import sys
sys.path.append(liblocation)
import ESC_selectObjsForExport
import pymel.core as pm
import os

# Set RMS Debug level
os.environ['RMSDEBUG'] = '1'

def importAllReferences():
    log.info("Importing all references...")
    # Import all references in file
    done = False
    while (done == False and (len(pm.listReferences()) != 0) ):
        refs = pm.listReferences()
        log.info("Importing " + str(len(refs)) + " references.")
        for ref in refs:
            if ref.isLoaded():
                done = False
                ref.importContents()
            else:
                done = True
    log.info("Done importing references...")
    return True

def ABCPyCallback(frameno):
    log.info("ABC Exporting frame number: %s"%(frameno))

def exportABC(objs, startFrame, endFrame, ABC_LOC):
    rootsStr = ""
    objs = pm.ls(sl=True)
    for obj in objs:
        rootsStr += " -root %s"%(obj.name())
    abcCommand = 'AbcExport -j "-writeVisibility -uv -worldSpace ' + \
            '-pfc ABCPyCallback(#FRAME#) ' + \
            '-frameRange %s %s %s -file %s"'%(startFrame, endFrame, \
                                             rootsStr, ABC_LOC)
    log.info(abcCommand)
    print abcCommand
    log.info("Writing ABC data to file: "+ ABC_LOC)
    pm.mel.eval(abcCommand)

def storeShaders():
    print "Storing shaders"
    objects = pm.ls(g=1)
    shaders = {}
    for obj in objects:
        if(len(obj.shadingGroups()) > 0):
            shaders[str(obj)] = map(str, obj.shadingGroups())
    return shaders

def exportShaders(MATS_LOC):
    shaders = pm.ls(materials=1)
    selection = []
    # Select all shaders that are attatched to meshes.
    for shd in shaders:
        grps = shd.shadingGroups()
        for grp in shd.shadingGroups():
            for member in grp.members():
                if("Mesh" in str(repr(member))):
                    selection.append(shd)
                    selection.append(grp)
    pm.select(clear=1)
    pm.select(selection, ne=1)
    pm.exportSelected(OUT_FILE, shader=1, force=1)

def restoreShaders(shadersDict):
    objsInScene = set(map(str, pm.ls()))
    for obj, shs in shadersDict.iteritems():
        if ( str(obj) in objsInScene ):
            for shader in shs:
                if (str(shader) in objsInScene):
                    pm.select(obj)
                    pm.sets(shader, fe=1)


def run(fileName, ABC_LOC, MATS_LOC, OUT_FILE):
    # Load plugins
    pm.loadPlugin("AbcExport")
    pm.loadPlugin("AbcImport")

    # Loading the file.
    log.info("Maya now opening file: \n" + fileName)
    pm.openFile(fileName, force=1)

    # Import all references.
    importAllReferences()

    # Build a list of all of the exportable geometry in the scene.
    ABCExportObjs = ESC_selectObjsForExport.run()

    # Get the start frame and end frame
    startFrame = pm.playbackOptions(q=1, minTime=True) 
    startFrame -= 5 # Adjust to allow for preroll
    log.info("First frame of shot is: %s"%(startFrame))
    endFrame = pm.SCENE.defaultRenderGlobals.endFrame.get()
    endFrame = pm.playbackOptions(q=1, maxTime=True) 
    log.info("Last frame of shot is: %s"%(endFrame))

    # Alembic export it
    exportABC(ABCExportObjs, startFrame, endFrame, ABC_LOC)

    # Export Shaders
    log.info("Writing shaders to file..." + fileName)
    exportShaders(MATS_LOC)

    # Store the shaders for re-application later.
    log.info("Storing the shaders for re-application..." + fileName)
    shadersDict = storeShaders()

    # Save the file
    log.info("Maya now saving file: \n" + fileName)
    pm.saveFile(force=1, type="mayaBinary")

    # Make a new file
    log.info("Creating new file..." + fileName)
    #pm.newFile(force=1)
    pm.openFile(OUT_FILE, force=1)

    # Import ABC Cache
    log.info("Importing ABC cache..." + fileName)
    pm.mel.eval('AbcImport -ftr -d "%s"'%(ABC_LOC))

    # Re-apply the shaders
    log.info("Re-applying shaders..." + fileName)
    restoreShaders(shadersDict)

    # Save the file
    log.info("Saving the maya file." + fileName)
    pm.saveFile(force=1, type="mayaBinary")

    # Close Maya
    os._exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        log.info("I'm sorry, you must provide a file to work with.")
        sys.exit()

    fileName = sys.argv[1]
    ABC_LOC = sys.argv[2]
    MATS_LOC = sys.argv[3]
    OUT_FILE = sys.argv[4]
    run(fileName, ABC_LOC, MATS_LOC, OUT_FILE)
