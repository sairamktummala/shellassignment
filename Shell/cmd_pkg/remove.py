import os 
import sys
def remove(file):
    if os.path.exists(file):
         os.remove(file)
    else:
        sys.stdout.write('file not found')
        sys.stdout.write('\n')