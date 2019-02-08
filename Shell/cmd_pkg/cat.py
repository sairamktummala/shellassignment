import sys
import os
path = os.getcwd()
def catfun(file):
    if os.path.isfile(file):
        data=open(file)
        sys.stdout.write(data.read())
        sys.stdout.write('\n')
    else:
        sys.stdout.write(file)
        sys.stdout.write('\033[1;31;40m  :No such File exist\033[1;m')
        sys.stdout.write('\n')
def catfun2(cmd):
    content=''
    for i in range(1,len(cmd)):
        if os.path.isfile(cmd[i]):
            data=open(cmd[i])
            content+=(data.read())
        else:
            sys.stdout.write('\033[1;31;40m ')
            sys.stdout.write(cmd[i])
            sys.stdout.write(':No such File exist\033[1;m')
            sys.stdout.write('\n')
    sys.stdout.write(content)
    sys.stdout.write('\n')

