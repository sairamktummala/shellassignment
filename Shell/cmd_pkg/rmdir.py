import os
import sys
def removedir(file):
    if os.path.exists(file):
        os.rmdir(file)
    else:
        sys.stdout.write(file)
        sys.stdout.write(': No such directory exists')
        sys.stdout.write('\n')