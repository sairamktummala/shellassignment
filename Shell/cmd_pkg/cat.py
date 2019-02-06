import sys
def catfun(file):
    data=open(file)
    sys.stdout.write(data.read())
    sys.stdout.write('\n')