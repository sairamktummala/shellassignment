#!/usr/bin/env python
from cmd_pkg.commands import *
import sys
import threading
import multiprocessing 

def run_command(command,args=None,flags=None):
    #sys.stdout.write(str(command))
    if args:
        c = threading.Thread(target=command, args=(args))
    else:
        c = threading.Thread(target=command)
    c.start()
    c.join()

    
def executeCommand(cmd,history):
    history+=cmd
    history+=('\n')
    cmd = cmd.split()
    if(cmd[0]=='exit'):
        exit()
    
    #cat command
    if(cmd[0]=='cat'):
        run_command(catfun,(cmd,))
    
    #ls command
    if(cmd[0]=='ls'):
        if(len(cmd)>1):
            run_command(lsflag,(cmd,))
        else:
            run_command(lsfun)
    
    #wc command
    if(cmd[0]=='wc'):
        run_command(wcfun,(cmd,))
    
    #tail command
    if(cmd[0]=='tail'):
        run_command(tailfun,(cmd,))
    
    #head command
    if(cmd[0]=='head'):
        run_command(headfun,(cmd,))
    
    #rm command
    if(cmd[0]=='rm'):
        run_command(rm,(cmd,))
    
    #rmdir command
    if(cmd[0]=='rmdir'):
        run_command(removedir,(cmd,))
    
    #pwd function
    if(cmd[0]=='pwd'):
        run_command(pwdfun)
    
    #mkdir function
    if(cmd[0]=='mkdir'):
        run_command(makedir,(cmd,))
    
    #cd function
    if(cmd[0]=='cd'):
        run_command(cdfun,(cmd,))
    
    #mv function
    if(cmd[0]=='mv'):
        run_command(mvfun,(cmd,))
    
    #cp function
    if(cmd[0]=='cp'):
        run_command(cpfun,(cmd,))
    
    #less function
    if(cmd[0]=='less'):
        run_command(lessfun,(cmd,))
    
    #grep function
    if(cmd[0]=='grep'):
        run_command(grepfun,(cmd,))
    
    #history
    if(cmd[0]=='history'):
        run_command(historyfun(cmd,history))
    
    #sort
    if(cmd[0]=='sort'):
        run_command(sortfun,(cmd[1],))
    
    #who
    if(cmd[0]=='who'):
        run_command(whofun)

if __name__ == '__main__':
    history=[]
    while True:
        cmd = input('% ')
        if '|' in cmd or '<' in cmd or '>' in cmd or '>>' in cmd:
            sys.stdout.write('idi done')
        else:
            executeCommand(cmd,history)