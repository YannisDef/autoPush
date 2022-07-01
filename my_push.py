#!/bin/python3
import subprocess
import sys

def checkFTTest():
    print("FIRST STEP: TF")
    functionnalResult = subprocess.run(["./tests/functionnal_tests/mouli.sh"], capture_output=True)

    TFResult = str(functionnalResult)
    TFResult = TFResult.split('%')[0]
    TFResult = TFResult[TFResult.rfind(' '):len(TFResult)]

    if int(TFResult) == 100:
        checkUTTest()
    else:
        print("\t[ERROR]: all unit tests are not OK")
        subprocess.run(["./tests/functionnal_tests/mouli.sh"])

def checkUTTest():
    print("\tYes c'est validé :)")
    print("\nSECOND STEP: TU")
    unitTestResult = str(subprocess.run(["make", "tests_run"], capture_output=True))
#    UTResult = str(unitTestResult)
    UTResult = unitTestResult[unitTestResult.rfind("Tested"):len(unitTestResult)]

    tests = UTResult[UTResult.find('m') + 1:len(UTResult)]
    tests = tests[0:tests.find('\\')]

    UTResult = UTResult[UTResult.find("Passing"):len(UTResult)]

    passing = UTResult[UTResult.find('m') + 1:len(UTResult)]
    passing = passing[0:passing.find('\\')]

    if tests == passing:
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
