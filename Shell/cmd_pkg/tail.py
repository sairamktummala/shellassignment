import sys
def tailfun1(file):
    with open(file) as fvar:
        for lines in fvar:
            sys.stdout.write(lines)
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
  