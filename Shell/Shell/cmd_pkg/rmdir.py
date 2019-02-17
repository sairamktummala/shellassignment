import os
import sys
def removedir(command):
    file=command[1]
    if os.path.exists(file):
        os.rmdir(file)
    else:
        sys.stdout.write(file)
        sys.stdout.write(': No such directory exists')
        sys.stdout.write('\n')