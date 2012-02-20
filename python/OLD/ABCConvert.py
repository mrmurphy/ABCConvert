################################################################################
# Design for alembic pipeline script.
# Author, Murphy Randle, 2011
################################################################################
#############################################
######### Configuration options #############
loglocation = "/grp5/estefan/logs/conversions.log"
liblocation = "/grp5/estefan/tools/converter/lib/"
loglevel = "INFO"
#############################################

import sys
import shutil
import os
import subprocess
import datetime
import logging
import getpass

# Set up the logger:
log = logging.getLogger('log')
log.setLevel(getattr(logging, loglevel))
handler = logging.FileHandler(loglocation)
formatter = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

# Append to the path
sys.path.append(liblocation)

def WriteLogHeader(shotfile):
    log.info("\n\n\nUser %s \nconverting shot: %s\n on date: %s\n\n\n" \
		%(getpass.getuser(), shotfile, str(datetime.datetime.now())))

def main(filePath, OUT_FILE):
    WriteLogHeader(filePath)
    ########################################
    ### Get the file name and path
    ########################################
    pathStem = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)[:-3]
    # Establish the location for material export
    CACHE_DIR = os.path.join(pathStem, "cache")
    MATS_LOC = os.path.join(CACHE_DIR, fileName + "_MATS.mb")
    # Make a directory, and set location for ABC cache
    if not (os.path.isdir(CACHE_DIR)):
        os.mkdir(CACHE_DIR)
    ABC_LOC = os.path.join(CACHE_DIR, fileName + ".abc")
    ########################################
    ########################################

    ########################################
    ### CARRY OUT IMPORTANT PLANS
    ########################################
    ExportData(filePath, MATS_LOC, ABC_LOC, OUT_FILE)
    return True


def ExportData(filePath, MATS_LOC, ABC_LOC, OUT_FILE):
    log.info("Phase 1: Export data to disk.")
    log.info("Will export materials to: " + MATS_LOC)
    log.info("Will export ABCache to: " + ABC_LOC)
    log.info("Will make output file: " + OUT_FILE)
    # Copy animation file to temp file.
    fromFile = filePath
    pathStem = filePath[:-3]
    TEMP_FILE = pathStem + "_tempABC_.mb"

    if not os.path.exists(filePath):
        log.error("Oh, my. That file doesn't exist")
        sys.exit();

    shutil.copy(fromFile, TEMP_FILE)
    
    try:
        # Build command to execute maya
        log.info("Calling Maya.")
        subprocess.call(["mayapy", liblocation + 'ESC_ExportData_MAYA.py', TEMP_FILE,\
                         ABC_LOC, MATS_LOC, OUT_FILE])
    
        # Delete temp animation file
        os.remove(TEMP_FILE)
        log.info("Removing: " + TEMP_FILE)

    except(RuntimeError):
        log.error("I'm sorry, there was an unkown problem.")
        os.remove(TEMP_FILE)
        log.info("Removing: " + TEMP_FILE)
