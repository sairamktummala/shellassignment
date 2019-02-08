import os 
import sys
import shutil
import pathlib
import fnmatch
path=os.getcwd()
def rm(param):
    if '*' not in param:
        removeFile(param)
    if(param == 'r*' ):
        removeAllFilesInDirectory()
    if ('*' in param):
        removeSpecificFiles(param)
    
def removeAllFilesInDirectory():
    currentDirectory=pathlib.Path('.')
    shutil.rmtree(currentDirectory)
        
def removeSpecificFiles(param):
    Filesindirectory=os.listdir('.')
    count = 0
    for file in Filesindirectory:
        if fnmatch.fnmatch(file,param):
            count+=1
            os.remove(file)
        else:
            sys.stdout.write('rm: cannot remove ')
            sys.stdout.write(param)
            sys.stdout.write(': No such file or directory')
            sys.stdout.write('\n')

    
def removeFile(file):   
    if os.path.exists(file):
        os.remove(file)
    else:
        sys.stdout.write('file not found')
        sys.stdout.write('\n')