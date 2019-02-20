import sys
import os
import re


def headfun1(file):
    linelist = []
    with open(file) as fvar:
        lineCount = 0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    linelist = linelist[:10]
    for l in linelist:
        sys.stdout.write(l)

def headfun2(file,count):
    linelist = []
    with open(file) as fvar:
        lineCount=0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    linelist = linelist[:int(count)]
    for l in linelist:
        sys.stdout.write(l)  



def headfun1write(file,write,writefile):
    linelist = []
    returnstri=""
    with open(file) as fvar:
        lineCount = 0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    linelist = linelist[:10]
    for l in linelist:
        returnstri+=l
    
    writefile=writefile.strip()
    if(write==1):
        print('inside write')
        with open(writefile, 'w') as f:
            f.write(returnstri)
    elif(write==2):
        with open(writefile,'a') as f:
            f.write(returnstri)
    elif(write==3):
        return returnstri

def headfun2write(file,count,write,writefile):

    linelist = []
    returnstri=""
    with open(file) as fvar:
        lineCount=0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    linelist = linelist[:int(count)]
    for l in linelist:
        returnstri+=l
    
    writefile=writefile.strip()
    if(write==1):
        with open(writefile, 'w') as f:
            f.write(returnstri)
        
    elif(write==2):
        with open(writefile,'a') as f:
            f.write(returnstri)
    elif(write==3):
        return returnstri