#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by galbrecht on 2009-06-29.
Copyright (c) 2009 splunk. All rights reserved.
"""

import sys
import getopt
import pexpect
import sys
import random

help_message = '''
ports = range of ports to perform operation on, comma separated. e.g: 1,24
op = operation to perform: bump, up, down
'''


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

class PortOperations(object):
    def __init__(self,switch,password,ports):
        self.ports = ports
        self.password = password
        self.switch = switch
        self.child = pexpect.spawn('telnet ' + self.switch)
        #self.child.logfile = sys.stdout
        self.child.expect('Password:')
        self.child.sendline(self.password)
        self.child.expect('stressSwitch>')
        self.child.sendline("en")
        self.child.expect('Password:')
        self.child.sendline(self.password)
        self.child.expect('stressSwitch#')
        self.child.sendline("config t")
        self.child.expect('#')
        
    def __del__(self):
        self.child.sendline("exit")

    def portCmd(self,port,cmd):
        self.child.sendline("int fa0/" + str(port))
        self.child.expect('#')
        self.child.sendline(cmd)
        print "port:%s %s" % (port,cmd)

    def func_up(self):
        for port in self.ports:
            self.portCmd(port,'no shutdown')
            
    def func_down(self):
        for port in self.ports:
            self.portCmd(port,'shutdown')

    def func_bump(self):
        #/opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/
        randPort = str(random.randrange(self.ports[0],self.ports[-1]))
        cmd = "shutdown"
        if random.random() > random.random():
            cmd = "no shutdown"
        self.portCmd(randPort,cmd)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "p:o:", ["ports=","op=","--operation"])
        except getopt.error, msg:
            raise Usage(msg)
    
        op = 'bump'
        ports = range(1,24)
        password = 'taco'
        switch = '10.1.7.254'
        
        # option processing
        for option, value in opts:
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-p","--ports"):
                ports = range(value.split(',')[0],value.split(',')[1])
            if option in ("-o", "--op","--operation"):
                op = value

        print "Operation: %s" % op
        print "Ports: %s" % ports
        
        portObj = PortOperations(switch,password,ports)
        
        try:
            _result = getattr(portObj, 'func_' + op)()
        except AttributeError, e:
            pass
            #mLogger.debug("%s - adHoc command exited for this reason (may not be an error): %s" % (__LogPrfx,e,))
            #_result = getattr(portObj, 'func_help')()
            
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())
