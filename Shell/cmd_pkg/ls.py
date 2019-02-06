import os
import sys
import stat
def lsfun():
    filename=os.listdir('.')
    for name in filename:
            sys.stdout.write(name)
            sys.stdout.write('\n')
