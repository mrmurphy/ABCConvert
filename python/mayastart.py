import sys
import os
sys.path.append("python/")
import Shot

curshot = Shot.Shot(sys.argv[1])
curshot.run()
os._exit(0);
