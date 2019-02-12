import sys
import os
 
def wcfun(cmd):
        if(len(cmd)>2):
                wcfun2(cmd)
        else:
                wcfun1(cmd[1])



def wcfun1(file):
        countLines = 0
        countWords = 0
        count_char = 0
        if os.path.exists(file):    
                with open(file) as var:
                        lines=var.readlines()
                with open(file) as data:
                        for line in data:
                                count_char += len(line)
                                words=line.split()
                                countWords += len(words)
                                count_char+=1 
                count_char -= 1         
                count_Lines = len(lines) - 1
                sys.stdout.write('  ')
                sys.stdout.write(str(count_Lines))
                sys.stdout.write(' ')
                sys.stdout.write(str(countWords))
                sys.stdout.write(' ')
                sys.stdout.write(str(count_char))
                sys.stdout.write(' :')
                sys.stdout.write(file)
                sys.stdout.write('\n')    
             

        else:
                sys.stdout.write(file)
                sys.stdout.write(': No such file exists \n')


def wcfun2(cmd):
        countLines = 0
        countWords = 0
        count_char = 0
        if os.path.exists(cmd[1]):
                with open(cmd[1]) as var:
                        lines=var.readlines()
                with open(cmd[1]) as data:
                        for line in data:
                                count_char += len(line)
                                words=line.split()
                                countWords += len(words)
                                count_char+=1  
                count_char -= 1         
                count_Lines = len(lines) - 1
                if cmd[2] == '-l':
                        sys.stdout.write(str(count_Lines))
                        sys.stdout.write(' :  ')
                        sys.stdout.write(str(cmd[1]))
                        sys.stdout.write('\n')
                elif cmd[2] == '-w':
                        sys.stdout.write(str(countWords))
                        sys.stdout.write(' :  ')
                        sys.stdout.write(str(cmd[1]))
                        sys.stdout.write('\n')
                elif cmd[2] == '-m':
                        sys.stdout.write(str(count_char))
                        sys.stdout.write(' :  ')
                        sys.stdout.write(str(cmd[1]))
                        sys.stdout.write('\n')
        else:
                sys.stdout.write(str(cmd[1]))
                sys.stdout.write(': No such file exists \n')
        