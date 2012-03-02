import sys
import os
sys.path.append("python/")
import Shot
curshot = Shot.Shot('/grp7/projectsmurp/ABCConvert/unittest/unittest.mb')
curshot.run()
print "Hello!"

os._exit(0);
