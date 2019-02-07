#!/usr/bin/env python
from cmd_pkg.commands import *
import sys
if __name__ == '__main__':  
    while True:
        cmd = input('% ')
        cmd = cmd.split()
        if(cmd[0]=='exit'):
            break 
        if(cmd[0]=='cat'):
            catfun(cmd[1])
        if(cmd[0]=='ls'):
            if(len(cmd) > 1):
                if(cmd[1]=='l'):
                    lslfun()
                elif(cmd[1]=='a'):
                    lsafun()

            else:
                lsfun()
        if(cmd[0]=='wc'):
            wcfun(cmd[1])
        if(cmd[0]=='tail'):
            if(len(cmd) > 2):
                tailfun2(cmd[1],cmd[2])
            else:
                tailfun1(cmd[1])
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
        if(cmd[0]=='cp'):
            cpfun(cmd[1],cmd[2])
