import sys
import os
sys.path.append("python/")
import Shot
curshot = Shot.Shot('/grp5/estefan/production3d/users/murphyra/C_17_Animation.mb')
curshot.run()
print "Hello!"

os._exit(0);
