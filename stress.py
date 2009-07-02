#!/usr/bin/env python
# encoding: utf-8
"""
stress.py

Created by galbrecht on 2009-06-22.
Copyright (c) 2009 splunk. All rights reserved.
"""

import sys
import os
from subprocess import Popen, PIPE
import random
import socket

def main():
    stressHosts_by_host = ['hulk','tool','me-too','sfeserv27','sfeserv03','gba-ubun810-amd64','gba-ubun810-i386','gba-mac-ppc','gba-macpro','qa-macmini','gba-fbsd63-i386', \
    'gba-fbsd72-i386','sfeserv35','qa-vfbsd63-i386','qa-vfbsd63-amd64','qa-vubun810-i386','qa-vubun810-amd64','qa-vfc9-i386','qa-vcent52-amd64','qa-vubun904-i386','qa-vubun904-amd64']
    
    stressHosts = []
    for sh in range(1,16):
        try:
            stressHosts.append(socket.gethostbyname('stress%02d.splunk.com' % sh))
        except socket.gaierror:
            pass
    
    # do the same for pre-defined hosts
    for sh in stressHosts_by_host:
        try:
            stressHosts.append(socket.gethostbyname(sh))
        except socket.gaierror:
            pass
    
    random.shuffle(stressHosts)
    
    dns = "server sfeserv31.splunk.com\nzone es.splunk.com\nupdate delete stressclients.es.splunk.com. A\n"
    
    IPs = ''
    for IP in stressHosts:
        IPs = "update add stressclients.es.splunk.com. 3600 A %s\n %s" % (IP,IPs)
    dns = dns + IPs + "show\nsend\nEOF"
    
    std_pipes = {}
    cmd = ["nsupdate","-k","Kes.splunk.com.+157+51549.key"]
    #try:
    po = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    std_pipes = po.communicate(input=dns)
    print std_pipes

if __name__ == '__main__':
    main()

