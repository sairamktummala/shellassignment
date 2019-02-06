import os
import sys
def makedir(file):
    if not os.path.exists(file):
        os.makedirs(file)
    else:
        sys.stdout.write('Directory already exists')