import pymel.core as pm
# The goal here is to select all geometry in the scene for Alembic export 
# except objects which are parented underneath a top leaf node.

# Important, in order for this to work, any rigs in the
# scene must have _rig in their name, and hold all of
# their GEO in a group called _rig:Geo or some acceptable
# variation (see the regex below).

def ESC_addRigGeo():
    sel = pm.ls(regex='*_[rR]igs*\d*[_:][Gg]eo')
    return sel

def ESC_addOtherGeo():
    # Add any non-character geo
    retsel = []
    geolist = pm.ls(g=True, v=True)
    for geo in geolist:
        if ("_rig" not in geo.name() and \
            "_Rig" not in geo.name() ):
            # This is important, I only want to select
            # the top-most transform node for alembic 
            # export. That's what this command does.
            parent = geo.getParent(-1)
            if ("_rig" not in parent.name() and \
                "_Rig" not in parent.name()):
                retsel.append(parent)
    return retsel

def ESC_Cameras():
    # Select any non-default cameras
    excludes = ["persp","top","front","side"]
    retsel = []
    camlist = pm.ls(ca=True)
    for cam in camlist:
        exclude = False
        for exname in excludes:
            if cam.startswith(exname):
                exclude=True
        if not exclude:
            retsel.append(cam.getParent(-1))
    return retsel
    


#main:

def run():
    print "\n What's going on? \n"
    pm.select(clear=True)
    sel = []

    # Get geo in the scene.
    sel = (ESC_addOtherGeo())
    # Get geo from rigs.
    rigGeo = ESC_addRigGeo()
    if len(rigGeo) != 0:
        sel.append(rigGeo)
    # Get animation cameras, or layout.
    cams = ESC_Cameras()
    if len(cams) != 0:
        sel.append(cams)
    pm.select(sel)
    return sel
run()
