#!/usr/bin/env python
from cmd_pkg.commands import *
import sys

def executeCommand(cmd,history):
    history+=cmd
    history+=('\n')
    cmd = cmd.split()
    if(cmd[0]=='exit'):
        exitfun()
    if(cmd[0]=='cat'):
        catfun(cmd)
    if(cmd[0]=='ls'):
        if(len(cmd)>1):
            lsflag(cmd)
        else:
            lsfun()
    if(cmd[0]=='wc'):
        wcfun(cmd)
    if(cmd[0]=='tail'):
        if(len(cmd) > 2):
            tailfun2(cmd[1],cmd[2])
        else:
            tailfun1(cmd[1])
    if(cmd[0]=='head'):
        if(len(cmd) > 2):
            headfun2(cmd[1],cmd[2])
        else:
            headfun1(cmd[1])
    if(cmd[0]=='rm'):
        rm(cmd[1])
    if(cmd[0]=='rmdir'):
        removedir(cmd[1])
    if(cmd[0]=='pwd'):
        pwdfun()
    if(cmd[0]=='mkdir'):
        makedir(cmd[1])
    if(cmd[0]=='cd'):
        length = len(cmd)
        if(length == 1):
            cdfun()
        else:
            if(cmd[1]=='~'):
                cdfun()
            elif(cmd[1]=='..'):
                cdfun2()
            else:
                cdfun3(cmd[1])
    if(cmd[0]=='mv'):
        mvfun(cmd[1],cmd[2])
        historyfun(cmd,0)
    if(cmd[0]=='cp'):
        cpfun(cmd[1],cmd[2])
    if(cmd[0]=='less'):
        lessfun(cmd[1])
    if(cmd[0]=='grep'):
        grepfun(*cmd)
    if(cmd[0]=='history'):
        historyfun(cmd,history)
    if(cmd[0].startswith('!')):
        sys.stdout.write('has!')
    if(cmd[0]=='sort'):
        tempstr = sortfun(cmd[1])
    sys.stdout.write(tempstr)

if __name__ == '__main__':
    history=[]
    while True:
        cmd = input('% ')
        if '|' in cmd or '<' in cmd or '>' in cmd or '>>' in cmd:
            sys.stdout.write('idi done')
        else:
            executeCommand(cmd,history)
   