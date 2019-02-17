import sys
import os
def pwdfun():
    returnString=os.getcwd()
    sys.stdout.write(returnString)
    sys.stdout.write('\n')
def pwdrefun():
    returnString=os.getcwd()
    return returnString
    
