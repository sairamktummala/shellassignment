import os 
import sys
def sortfun(file):
    strsort=""
    if os.path.exists(file):
        with open(file) as fvar:
            lines=fvar.readlines()
            lines.sort()
            for i in lines:
                strsort+=i
        sys.stdout.write(strsort)
        fil=open(file,'w')
        fil.write(strsort)

    else:
        sys.stdout.write('file not found')
        sys.stdout.write('\n')
    return strsort
