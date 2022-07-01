#!/bin/python3
import subprocess
import sys

def checkFTTest():
    print("FIRST STEP: TF")
    functionnalResult = str(subprocess.run(["./tests/functionnal_tests/mouli.sh"], capture_output=True)).split('%')[0]
    functionnalResult = functionnalResult[functionnalResult.rfind(' '):len(functionnalResult)]

    if int(functionnalResult) == 100:
        checkUTTest()
    else:
        print("\t[ERROR]: all unit tests are not OK")
        subprocess.run(["./tests/functionnal_tests/mouli.sh"])

def checkUTTest():
    print("\tYes c'est validé :)")
    print("\nSECOND STEP: TU")
    unitTestResult = str(subprocess.run(["make", "tests_run"], capture_output=True))

    UTResult = unitTestResult[unitTestResult.rfind("Tested"):len(unitTestResult)]
    strPercent = UTResult[UTResult.find('m') + 1:len(UTResult)]
    nbTests = strPercent[0:strPercent.find('\\')]
    UTResult = UTResult[UTResult.find("Passing"):len(UTResult)]
    nbTestsOK = strPercent[0:strPercent.find('\\')]

    if nbTests == nbTestsOK:
        githubCommands()
    else:
        print("\t[ERROR]: all fonctional tests are not OK")
        subprocess.run(["./tests/functionnal_tests/mouli.sh"])

def githubCommands():
    print("\tYes c'est validé :)")
    args = sys.argv
    for i in range(1, len(args)):
        subprocess.run(["git", "add", args[i]])
    subprocess.run(["git", "commit"])
    subprocess.run(["git", "push"])

if __name__ == '__main__':
    checkFTTest()
