import os
import sys
import glob
import re

# need argv

filesToProcess = glob.glob( os.path.join(sys.argv[1],'*.py') )

re_pattern = re.compile(r"^\ +(?P<prntStmt>print\ +[^\n\r]+)$")

for fileToProcess in filesToProcess:
    if os.path.isfile(fileToProcess) and not fileToProcess == sys.argv[0]:
        inFile = open(fileToProcess,'r')
        for lineInFile in inFile:
            re_match = re_pattern.search(lineInFile)
            if re_match:
                prntStmt = re_match.group('prntStmt')
                if prntStmt.find('>>') == -1:
                    print re.sub(r"^print","logger.info(",
                                                        re.sub(r"$"," )",prntStmt))
                    #print prntStmt.replace('print','logger.info(').replace('
                    #print prntStmt
        inFile.close()
