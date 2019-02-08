import shutil
import os
import sys
path=os.getcwd()
def cpfun(file1,file2):
    if os.path.isfile(file1):
        shutil.copyfile(file1,file2)
    else:
        sys.stdout.write('\033[1;31;40m cp: cannot stat ')
        sys.stdout.write(file1)
        sys.stdout.write('\033[1;31;40m :No such File exist\033[1;m')
        sys.stdout.write('\n')    

    