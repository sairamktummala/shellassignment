import shutil
import os
import sys
path=os.getcwd()
def mvfun(command):
    file1=command[1]
    file2=command[2]
    shutil.move(file1,file2)
    