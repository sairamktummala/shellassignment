import os
import sys
import stat
import time
from stat import *
def lslfun():
    path=os.getcwd()
    files=[]
    files=os.listdir(path)
    for x in range(0,len(files)):
        filename=files[x]
        checkMode(filename)
        #s = str(oct(os.stat(filename)[stat.ST_MODE]))
        #sys.stdout.write(s)
        sys.stdout.write("\n")
        """
        digits=[int(s[0]),int(s[1]),int(s[2])]
        lookup=['','x','w','wx','r','rx','rw','rwx']
        uout=lookup[digits[0]]
        gout=lookup[digits[1]]
        oout=lookup[digits[2]]
        mode=str(uout+'-'+gout+'-'+oout)       
        filesize=str(os.stat(files[x]).st_size)
        timeMod=str(time.ctime(os.path.getmtime(filename)))
        #sys.stdout.write(filesize+'\t\t\t'+mode+'\t\t\t'+timeMod+'\t'+filename)
        sys.stdout.write("\n")
        """
def checkMode(filename):
    mode=os.stat(filename).st_mode
    perm=''
    if S_ISDIR(mode):
        perm='d'
        if(stat.S_IRWXG):
            if(stat.S_IWGRP):
                perm='-x'
  
    sys.stdout.write(perm)
    sys.stdout.write(filename)
