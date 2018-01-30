#!/usr/bin/env python 

import sys
import time

class Sleeper(object) :

    def __init__(self) :
        pass

    def wait(self, interval) :
        assert(interval >= 0 ) 
        time.sleep(interval)
        return 0



def main() :
    print 'hi'
    s = Sleeper()
    s.wait(3)
    print 'Bye'

if __name__ == '__main__' :
    sys.exit(main())

