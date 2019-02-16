import os
import getpass
import sys
def whofun(f):
    print(f)
    sys.stdout.write(getpass.getuser())