#!/bin/python3

#? FAIRE UNIT TEST
#?   si 100% -> FAIRE TEST FONCTIONNEL
#?   si != 100% -> PRINT "IMPOSSIBLE DE PUSH PROBLEME TU"
#?       si 100% -> git add les files ; git commit $1 ; git push origin master
#?       si != 100% -> PRINT "IMPOSSIBLE DE PUSH PROBLEME TF"

#i=1
#for arg in "$@"
#do
#    printf "argument $i: $arg\n"
#    i=$((i + 1 ))
#done

import subprocess
import sys

def checkFTTest():
    print("FIRST STEP: TF")
    functionnalResult = subprocess.run(["./tests/functionnal_tests/mouli.sh"], capture_output=True)

    TFResult = str(functionnalResult)
    TFResult = TFResult.split('%')[0]
    TFResult = TFResult[TFResult.rfind(' '):len(TFResult)]

    if int(TFResult) == 100:
        print("\tYes c'est validé :)")
        checkUTTest()
    else:
        print("\t[ERROR]: all unit tests are not OK")
        subprocess.run(["./tests/functionnal_tests/mouli.sh"])

def checkUTTest():
    print("\nSECOND STEP: TU")
    unitTestResult = subprocess.run(["make", "tests_run"], capture_output=True)
    UTResult = str(unitTestResult)
    UTResult = UTResult[UTResult.rfind("Tested"):len(UTResult)]

    tests = UTResult[UTResult.find('m') + 1:len(UTResult)]
    tests = tests[0:tests.find('\\')]

    UTResult = UTResult[UTResult.find("Passing"):len(UTResult)]

    passing = UTResult[UTResult.find('m') + 1:len(UTResult)]
    passing = passing[0:passing.find('\\')]

    if tests == passing:
        print("\tYes c'est validé :)")
        githubCommands()
    else:
        print("\t[ERROR]: all fonctional tests are not OK")
        subprocess.run(["./tests/functionnal_tests/mouli.sh"])

def githubCommands():
    args = sys.argv
    print(args)

    for i in range(2, len(args)):
        print("git add " + args[i])
        subprocess.run(["git", "add", args[i]])

    print("git commit " + args[1])
    commit = "\"" + args[1] + "\""
    print(commit)
#    subprocess.run(["git", "commit", "-m", commit])


    subprocess.run(["git", "push", "origin", "master"])
#    print("git push origin master")

if __name__ == '__main__':
    checkFTTest()