import os
import sys
import stat
import time
from stat import *
import time,subprocess,shutil

def lsfun():
    filename=os.listdir('.')
    for name in filename:
            if(name.startswith('.')):
                    pass
            else:
                    sys.stdout.write(name)
                    sys.stdout.write('\n')

def lsflag(cmd):
        
        if(cmd[1]=='-l'):
                lslfun()
        elif(cmd[1]=='-a'):
                lsafun()
        elif(cmd[1]=='-h'):
                lshfun()

def lsafun():
    dir=os.listdir('.')
    for name in dir:
            sys.stdout.write(name)
            sys.stdout.write('\n')
 
def lslfun():
        path=os.getcwd()
        files=os.listdir(path)
        for file in files:
                printablestr=""
                mode=os.stat(file).st_mode
                perm=''
                if S_ISDIR(mode):
                        perm='d'
                else:
                        perm='-'
                s = str(oct(os.stat(file)[stat.ST_MODE])[-3:])
                permission={'0' :'---', '1' : '--x', '2' : '-w-','3' : '-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
                userperm=permission[s[0]]
                groupperm=permission[s[1]]
                otherperm=permission[s[2]]
                permstring=perm+userperm+groupperm+otherperm
                printablestr+=permstring             
                
                stlin=str(os.stat(file)[stat.ST_NLINK])
                printablestr+=stlin
                printablestr+='\t'

                size= str(os.stat(file).st_size)
                printablestr+=size

                printablestr+='\t'

                modifiedTime=str(time.ctime(os.path.getmtime(file)))
                printablestr+=modifiedTime

                printablestr+='\t'
                
                printablestr+=file
                sys.stdout.write(printablestr)
                sys.stdout.write('\n')     
def lshfun():
        path=os.getcwd()
        files=os.listdir(path)
        for file in files:
                printablestr=""
                mode=os.stat(file).st_mode
                perm=''
                if S_ISDIR(mode):
                        perm='d'
                else:
                        perm='-'
                s = str(oct(os.stat(file)[stat.ST_MODE])[-3:])
                permission={'0' :'---', '1' : '--x', '2' : '-w-','3' : '-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
                userperm=permission[s[0]]
                groupperm=permission[s[1]]
                otherperm=permission[s[2]]
                permstring=perm+userperm+groupperm+otherperm
                printablestr+=permstring             
                
                stlin=str(os.stat(file)[stat.ST_NLINK])
                printablestr+=stlin
                printablestr+='\t'

                size= str(os.stat(file).st_size)
                psize='0'
                if int(size)<1024:
                        psize=size+'B'
                elif int(size)<1048576:
                        psize=size[0]+'.'+size[1]+'K'
                elif int(size)>1048576:
                        psize=size[0]+'.'+size[1]+'GB'
                
                printablestr+=psize

                printablestr+='\t'

                modifiedTime=str(time.ctime(os.path.getmtime(file)))
                printablestr+=modifiedTime

                printablestr+='\t'
                
                printablestr+=file
                sys.stdout.write(printablestr)
                sys.stdout.write('\n')     
