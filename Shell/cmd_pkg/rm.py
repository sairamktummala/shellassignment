import os 
import sys
import shutil
import pathlib
import fnmatch
def rm(param):
    if(param == 'r' ):
        removeAllFilesInDirectory()
    if (param.find('*')|param.startswith('*')):
        removeSpecificFiles(param)
    else:
        removeFile(param)


def removeAllFilesInDirectory():
    sys.stdout.write('i am inside the loop')
    currentDirectory=pathlib.Path('.')
    shutil.rmtree(currentDirectory)
        
def removeSpecificFiles(param):
    listOfFiles=os.listdir('.')
    pattern=param
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry,pattern):
            sys.stdout.write(entry)

    
def removeFile(file):
    if os.path.exists(file):
        os.remove(file)
    else:
        sys.stdout.write('file not found')
        sys.stdout.write('\n')