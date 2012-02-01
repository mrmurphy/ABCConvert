#! /usr/bin/python
import Shot
import time
def test():
    print "This is fast."
    foo = Shot.Shot("Murphy_21")
    foo.run()
    print "Or maybe not?"
    while(foo.GetStatus() == "False"):
        print foo.GetLog()
        time.sleep(1)
    print foo.GetLog()

test()
