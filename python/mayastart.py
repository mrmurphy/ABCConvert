import sys
import os
sys.path.append("python/")
import Converter

curshot = Converter.Converter(sys.argv[1], sys.argv[2])
curshot.run()
os._exit(0);
