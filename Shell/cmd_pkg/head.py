import sys
def headfun(command):
        if len(command)>2 :
                headfun2(command[1],command[2])
        else:
                headfun1(command[1])

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