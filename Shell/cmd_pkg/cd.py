import os
def cdfun():
    os.chdir(os.path.expanduser("~"))
def cdfun2():
    os.chdir("..")
def cdfun3(path):
    os.chdir(path)