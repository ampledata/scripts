#!/usr/bin/env python2.6
# script to randomly shut/no shut ports on our catalyst switch (for stress testing)
# (c) 2009 greg albrecht <gba@gregalbrecht.com>

import pexpect
import sys
import random

#/opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/

randPort = str(random.randrange(1,23))

password = "taco\n"
child = pexpect.spawn('telnet 10.1.7.254')
#child.logfile = sys.stdout

child.expect('Password:')
child.sendline(password)
child.expect('stressSwitch>')
child.sendline("en\n")
child.expect('Password:')
child.sendline(password)
child.expect('stressSwitch#')
child.sendline("config t\n")
child.expect('#')
child.sendline("int fa0/" + randPort + "\n")
child.expect('#')
if random.random() > random.random():
	print "port:%s shutdown" % randPort
	child.sendline("shutdown\n")
else:
	print "port:%s no shutdown" % randPort
	child.sendline("no shutdown\n")
child.sendline("exit\n")
