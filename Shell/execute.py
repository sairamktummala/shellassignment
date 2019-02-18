#!/usr/bin/env python
from cmd_pkg.commands import *
import sys
import threading
import multiprocessing 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#execute command function takes function takes arguments like 
#command : which is to be performed
#history : once the command starts it is stored in history
#write : says how to write
 #write = 0 : writes on console
 #write = 1 : writes on a file with name write file
 #write = 2 : appends the result to write file
 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def executeCommand(command,history,write,writefile):
    history+=command
    history+=('\n')
    cmd = command.split()
    background=0
    
    #if a command has & in it then the command is executed in the background
    if '&' in cmd:
        background=1
        # & is popped out 
        cmd.pop()
    
    #if the command has --help then it directly goes into the help istead of executing
    if '--help' in cmd:
        #initialises the thread and the function to be called is given in the target followed by arguments to thee function
        c= threading.Thread(target=helpfun,args=(cmd[0],write,writefile))
        if background==1 :
            #makes command to be run in the background
            c.daemon=True
            c.start()
        elif background==0:
            #makes thread start execution and wait till the command completes
            c.start()
            c.join()
    
    #if its not help then execute the command
    else:

        #cat command
        if(cmd[0]=='cat'):
            if write==0:
                c = threading.Thread(target=catfun,args=(cmd,))
                if background==1 :
                    c.daemon=True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            else:
                c = threading.Thread(target=catfunwrite,args=(cmd,write,writefile))
                if background==1 :
                    c.daemon=True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
        
        #ls command
        if(cmd[0]=='ls'):
            if write==0:
                #if ls has flags then it calls the ls flag function
                if(len(cmd)>1):
                    c = threading.Thread(target=lsflag,args=(cmd,))
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
                #just ls
                elif len(cmd)==1:
                    c = threading.Thread(target=lsfun)
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
            #if the output is redirected to some file then call the following functions
            elif write > 0:
        
                if(len(cmd)>1):
                    c = threading.Thread(target=lsflagwrite,args=(cmd,write,writefile))
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
                elif len(cmd)==1:
                    c = threading.Thread(target=lsfunwrite,args=(write,writefile))
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
        #wc command
        if cmd[0]=='wc':
            if write==0 :
                c = threading.Thread(target=wcfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=wcfunwrite,args=(cmd,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()

        #tail command
        if cmd[0]=='tail':
            if write==0 :
                c = threading.Thread(target=tailfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c= threading.Thread(target=tailfunwrite,args=(cmd,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
    
        #head command
        if cmd[0]=='head':
            if write==0 :
                c = threading.Thread(target=headfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=headfunwrite,args=(cmd,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()

        #less function
        if(cmd[0]=='less' and background==0):
            if write==0 :
                c = threading.Thread(target=lessfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=lessfunwrite,args=(cmd,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()

        #rm command
        if cmd[0]=='rm':
            c = threading.Thread(target=rmfun,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
        #rmdir command
        if cmd[0]=='rmdir':
            c = threading.Thread(target=removedir,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
    
        #mkdir function
        if cmd[0]=='mkdir':
            c = threading.Thread(target=makedir,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
    
        #cd function
        if cmd[0]=='cd':
            c = threading.Thread(target=cdfun,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
    
        #mv function
        if cmd[0]=='mv':
            c = threading.Thread(target=mvfun,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()

        #cp function
        if cmd[0]=='cp':
            c = threading.Thread(target=cpfun,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
    
    
        #pwd function
        if cmd[0]=='pwd':
            if write==0 :
                c = threading.Thread(target=pwdfun)
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=pwdwrite,args=(write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
    
        #grep function
        if cmd[0]=='grep':
            if write==0 :
                c = threading.Thread(target=grepfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=grepfunwrite,args=(cmd,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
    

        #history
        if cmd[0]=='history':
            if write==0 :
                c = threading.Thread(target=historyfun,args=(cmd,history))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=historyfunwrite,args=(cmd,history,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()

        #sort
        if cmd[0]=='sort':
            if write==0 :
                c = threading.Thread(target=sortfun,args=(cmd[1],))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
                elif write>0:
                    c = threading.Thread(target=sortfunwrite,args=(cmd[1],write,writefile))
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()

        #who
        if cmd[0]=='who':
            if write==0 :
                c = threading.Thread(target=whofun)
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=whofunwrite,args=(write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
    
        #chmod
        if cmd[0]=='chmod':
            chmodfun(cmd)
        
        #exit
        if(cmd[0]=='exit' ):
            sys.exit()

#main function
if __name__ == '__main__':
    #let history be list which store the commnds history
    history=[]
    #the commands implemented in the shell are taken into args
    args=('cat','cd','chmod','cp','exit','grep','head','history','less','ls','mkdir','mv','pwd','rm','rmdir','who','wc','tail','sort')
    #run till true
    while True:
        #have a % symbol during the input
        cmd = input('% ')
        #checkcmd have the split version of the command it helps us to check wether the command implemented or not
        checkcmd = cmd.split()
        ccommand=checkcmd[0]
        
        #if the command is implemented
        if ccommand in args:
            #if piping is present
            if '|' in cmd :
                #the output of first command before pipe is redirected to a file called result
                write=1

                #split the commands and store each individual command in commandlist
                commandlist=cmd.split('|')

                #check how many command are there in pipe
                last = len(commandlist)-1

                #strip the empty places around the command
                command1 = commandlist[0].strip()

                #let the output be redirected to a result.txt file
                tempfile='result.txt'

                #execute the first command
                executeCommand(command1,history,1,tempfile)
                first = 1
                #if there are more than two commands then the while loop lets us executing the commands inbetween
                while first < last :
                    #execute the command in order
                    commandtemp=commandlist[first].strip()
                    tempcheck=commandtemp.split()
                    if tempcheck[0] in args:
                        commandtemp+=' '
                        commandtemp+=tempfile
                        executeCommand(commandtemp,history,1,tempfile)
                        first+=1
                    else:
                        print('bash: ',commandtemp,': command not found')
                #finally execute the las command and write the output on console
                commandlast = commandlist[last].strip()
                temcom=commandlast.split()
                if temcom[0] in args:
                    commandlast+=' '
                    commandlast+=tempfile
                    executeCommand(commandlast,history,0,cmd)
                else:
                    print('bash: ',commandlast,': command not found')
            
            
            #if there is not piping in between the commands
            else:
                
                write=0
                command=""
                #the commands result is appended to a specified file
                if '>>' in cmd:
                    cmd=cmd.split('>>')
                    write=2
                    command=cmd[0]
                    file=cmd[1]
                    executeCommand(command,history,write,file)
                elif '>' in cmd:
                    write=1
                    cmd=cmd.split('>')
                    command=cmd[0]
                    file=cmd[1]
                    executeCommand(command,history,write,file)
                elif '<' in cmd:
                    tempcommandlist = cmd.split('<')
                    tempcommand = tempcommandlist[0]
                    tempfilename = tempcommandlist[1].strip()
                    finalcommand = tempcommand + tempfilename
                    executeCommand(finalcommand,history,0,cmd)
                else :
                    executeCommand(cmd,history,write,cmd)
        else:
            
            print('bash: ',ccommand,': command not found')
        