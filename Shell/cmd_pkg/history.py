import sys

def historyfun(cmd,history):
    stringhistory=""
    for i in history:
        stringhistory+=i
    sys.stdout.write(stringhistory)