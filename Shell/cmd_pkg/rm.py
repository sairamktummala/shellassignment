import os 
import sys
import shutil
import pathlib
import fnmatch
def rm(param):
    if(param == 'r*' ):
        removeAllFilesInDirectory()
    if (param.find('*')|param.startswith('*')):
        removeSpecificFiles(param)
    else:
        removeFile(param)


def removeAllFilesInDirectory():
    currentDirectory=pathlib.Path('.')
    shutil.rmtree(currentDirectory)
        
def removeSpecificFiles(param):
    Filesindirectory=os.listdir('.')
    for file in Filesindirectory:
        if fnmatch.fnmatch(file,param):
            os.remove(file)

    
def removeFile(file):
    if os.path.exists(file):
        os.remove(file)
    else:
        sys.stdout.write('file not found')
        sys.stdout.write('\n')