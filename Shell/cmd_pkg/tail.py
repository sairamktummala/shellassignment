import sys
def tailfun1(file):
    linelist = []
    with open(file) as fvar:
        lineCount=0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    tempCOunt = int(lineCount) - 10
    linelist = linelist[tempCOunt:]
    for l in linelist:
        sys.stdout.write(l)
    sys.stdout.write('\n')

def tailfun2(file,count):
    linelist = []
    with open(file) as fvar:
        lineCount=0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    tempCOunt = int(lineCount) - int(count)
    linelist = linelist[int(tempCOunt):]
    for l in linelist:
        sys.stdout.write(l)
    sys.stdout.write('\n')
  