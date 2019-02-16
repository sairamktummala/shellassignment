#!/usr/bin/env python
from cmd_pkg.commands import *
import sys
import threading
import multiprocessing 

def run_command(command,args=None,flags=None):
    if args:
        c = threading.Thread(target=command, args=(args))
    else:
        c = threading.Thread(target=command)
    c.start()
    c.join()

def run_commandInBackground(command,args=None,flags=None):
    if args:
        c = threading.Thread(target=command, args=(args))
    else:
        c = threading.Thread(target=command)
    c.daemon=True
    c.start()
    
def executeCommand(cmd,history):
    history+=cmd
    history+=('\n')
    cmd = cmd.split()
    background=0
    if '&' in cmd:
        background=1
        cmd.pop()

    if(cmd[0]=='exit' ):
        exit()
    
    #cat command
    if(cmd[0]=='cat' and background==0):
        run_command(catfun,(cmd,))
    if(cmd[0]=='cat' and background==1):
        print('i am getting caleed tough')
        run_commandInBackground(catfun,(cmd,))
    
    #ls command
    if(cmd[0]=='ls'):
        if(len(cmd)>1 and background==0):
            run_command(lsflag,(cmd,))
        if(len(cmd)>1 and background==1):
            run_commandInBackground(lsflag,(cmd,))
        elif len(cmd)==1 and background==1:
            run_commandInBackground(lsfun)
        elif len(cmd)==1 and background==0:
            run_command(lsfun)

    
    #wc command
    if(cmd[0]=='wc' and background==0):
        run_command(wcfun,(cmd,))
    if(cmd[0]=='wc' and background==1):
        run_commandInBackground(wcfun,(cmd,))
    
    #tail command
    if(cmd[0]=='tail' and background==0):
        run_command(tailfun,(cmd,))
    if(cmd[0]=='tail' and background==1):
        run_commandInBackground(tailfun,(cmd,))
    
    #head command
    if(cmd[0]=='head' and background==0):
        run_command(headfun,(cmd,))
    if(cmd[0]=='head' and background==1):
        run_commandInBackground(headfun,(cmd,))
    
    #rm command
    if(cmd[0]=='rm' and background==0):
        run_command(rm,(cmd,))
    if(cmd[0]=='rm' and background==1):
        run_commandInBackground(rm,(cmd,))
    
    #rmdir command
    if(cmd[0]=='rmdir' and background==0):
        run_command(removedir,(cmd,))
    if(cmd[0]=='rmdir' and background==1):
        run_commandInBackground(removedir,(cmd,))
    
    #pwd function
    if(cmd[0]=='pwd' and background==0):
        run_command(pwdfun)
    if(cmd[0]=='pwd' and background==1):
        run_commandInBackground(pwdfun)
    
    #mkdir function
    if(cmd[0]=='mkdir' and background==0):
        run_command(makedir,(cmd,))
    if(cmd[0]=='mkdir' and background==1):
        run_commandInBackground(makedir,(cmd,))

    #cd function
    if(cmd[0]=='cd' and background==0):
        run_command(cdfun,(cmd,))
    if(cmd[0]=='cd' and background==1):
        run_commandInBackground(cdfun,(cmd,))

    #mv function
    if(cmd[0]=='mv' and background==0):
        run_command(mvfun,(cmd,))
    if(cmd[0]=='mv' and background==1):
        run_commandInBackground(mvfun,(cmd,))

    #cp function
    if(cmd[0]=='cp' and background==0):
        run_command(cpfun,(cmd,))
    if(cmd[0]=='cp' and background==1):
        run_commandInBackground(cpfun,(cmd,))

    #less function
    if(cmd[0]=='less' and background==0):
        run_command(lessfun,(cmd,))
    if(cmd[0]=='less' and background==1):
        run_commandInBackground(lessfun,(cmd,))

    #grep function
    if(cmd[0]=='grep' and background==0):
        run_command(grepfun,(cmd,))
    if(cmd[0]=='grep' and background==1):
        run_commandInBackground(grepfun,(cmd,))

    #history
    if(cmd[0]=='history' and background==0):
        run_command(historyfun(cmd,history))
    if(cmd[0]=='history' and background==1):
        run_commandInBackground(historyfun(cmd,history))

    #sort
    if(cmd[0]=='sort' and background==0):
        run_command(sortfun,(cmd[1],))
    if(cmd[0]=='sort' and background==1):
        run_commandInBackground(sortfun,(cmd[1],))

    #who
    if(cmd[0]=='who' and background==0):
        run_command(whofun)
    if(cmd[0]=='who' and background==1):
        run_commandInBackground(whofun)

if __name__ == '__main__':
    history=[]
    while True:
        cmd = input('% ')
        if '|' in cmd or '<' in cmd or '>' in cmd or '>>' in cmd:
            sys.stdout.write('idi done')
        else:
            executeCommand(cmd,history)