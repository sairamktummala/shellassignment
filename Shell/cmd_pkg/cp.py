import shutil
import os
import sys
path=os.getcwd()
def cpfun(command):
    file1=command[1]
    file2=command[2]
    if os.path.isfile(file1):
        shutil.copyfile(file1,file2)
    else:
        sys.stdout.write('\033[1;31;40m cp: cannot stat ')
        sys.stdout.write(file1)
        sys.stdout.write('\033[1;31;40m :No such File exist\033[1;m')
        sys.stdout.write('\n')    
def cpfunString(string,filename,flag):
    if(flag==0):
        with open(filename, 'w') as f:
            f.write(string)
    if(flag==1):
        if os.path.isfile(filename):
            with open(filename, 'a') as f:
                f.write(string)
        else:
            sys.stdout.write('\033[1;31;40m cp: cannot stat ')
            sys.stdout.write(filename)
            sys.stdout.write('\033[1;31;40m :No such File exist\033[1;m')
            sys.stdout.write('\n')