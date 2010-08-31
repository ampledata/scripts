#!/usr/bin/env python
"""Replace Python print statements with logger.info() statements.

Developers - Please stop using Python's print. Logger is much more versatile.

Why?
====
    http://blog.tplus1.com/index.php/2007/09/28/the-python-logging-module-is-much-better-than-print-statements/
    http://plumberjack.blogspot.com/2009/09/python-logging-101.html
    http://docs.python.org/library/logging.html

What does it do?
================
    p2l will iterate through every Python (.py) file in a directory and 'monkey-patch' every
    print statement with a logger.info() statement. 
    THIS IS NOT FOOL PROOF.
    You must test your code afterwards.

Usage
=====
    $ python print2logger.py /path/to/directory/with/py/files

Example
=======
    1) python print2logger.py ~/src/my_project
    All modified files will be suffixed with: .p2l.123456789.12
    2) cd ~/src/my_project
    3) diff main.py main.py.p2l.123456789.12
    ...stuff...
    4) python main.py.p2l.123456789.12
    ...hopefully there's no errors...
    5) cp main.py.p2l.123456789.12 main.py
    6) Done!
    
"""
import os
import sys
import glob
import re
import time

filesToProcess  = glob.glob( os.path.join(sys.argv[1],'*.py') )
re_pattern      = re.compile(r"^\ +(?P<prntStmt>print\ +[^\n\r]+)$")
ourTime         = str(time.time())

print "All modified files will be suffixed with: .p2l.%s" % ourTime

for fileToProcess in filesToProcess:
    if os.path.isfile(fileToProcess) and not fileToProcess == sys.argv[0]:
        inFile  = open(fileToProcess,'r')
        outFile = open('.'.join((fileToProcess,'p2l',ourTime)), 'w')
        for lineInFile in inFile:
            re_match = re_pattern.search(lineInFile)
            if re_match:
                prntStmt = re_match.group('prntStmt')
                if prntStmt.find('>>') == -1:
                    lggrStmt    = re.sub( r"^print","logger.info(", re.sub(r"$"," )",prntStmt) )
                    lineInFile  = lineInFile.replace(prntStmt,lggrStmt)
            outFile.write(lineInFile)
        inFile.close()
        outFile.close()
