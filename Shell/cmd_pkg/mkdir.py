import os
import sys
def makedir(command):
    file=command[1]
    if not os.path.exists(file):
        os.makedirs(file)
    else:
        sys.stdout.write('Directory already exists')