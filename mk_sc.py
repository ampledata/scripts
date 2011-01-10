#!/usr/bin/env python
# encoding: utf-8
"""
fix_messages.py

Created by Greg Albrecht on 2010-07-22.
Copyright (c) 2010 splunk. All rights reserved.
"""

import sys
import os
import re
import glob

def main():
    
    OUT1 = open('sc.conf', 'w')

    for app in glob.glob('tier_*'):
        tier = app.split('_')[1]
        sc_conf = """
[serverClass:tier_%s:app:%s]
whitelist.0 = *
stateOnClient = enabled
restartSplunkd = True
        """ % (tier,app)
        print sc_conf
        
        #if messages_rex.match(line):
        #    messages_rex.match(line).group(1)
        #    time_field  = messages_rex.match(line).group(1)
        #    line        = line.replace(time_field, "\n%s" % time_field)
        #    print line
            
        OUT1.write(sc_conf)

    OUT1.close()

if __name__ == '__main__':
	main()

