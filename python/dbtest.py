#! /usr/bin/python
import Shot
def test():
    print "This is fast."
    foo = Shot.Shot("Murphy_21")
    foo.run()
    print "Or maybe not?"
    print foo.GetLog()
test()
