import sys
import os
import re
retstrng = ""
def grepfun(*args):
    if(args[1]=='-l'):
        pattern=args[2]
        grepListing(pattern)
    else:
        pattern=args[1]
        stri =""
        for i in args[2:]:
            stri+=grepcheckfile(i,pattern)
        sys.stdout.write(stri)
def grepListing(pattern):
    path=os.listdir('.')
    strinf=""
    for file in path:
        if os.path.isfile(file):
            with open(file) as fvar:
                for lines in fvar:
                    line = re.findall(pattern,lines)
                    if not line:
                        pass 
                    else:
                        tempstring = file
                        strinf+=tempstring
                        strinf+=('\n')
        else:
            pass
    sys.stdout.write(strinf)


def grepcheckfile(file,pattern):
    if os.path.isfile(file):
        strin2 = grepGetThelist(file,pattern)
        return strin2
    elif os.path.exists(file):
        strngh = " "
        return strngh
    else:
        sys.stdout.write(file)
        sys.stdout.write('\033[1;31;40m  :No such File exist\033[1;m')
        sys.stdout.write('\n')
        strngh = " "
        return strngh
    
def grepGetThelist(file,pattern):
    strin=""
    with open(file) as fvar:
        lineCount = 0
        for lines in fvar:
            line = re.findall(pattern, lines)
            if not line:
                pass
            else:
                tempstring = file + ":" + str(lines)
                strin+=tempstring
    strin+=('\n')
    return strin