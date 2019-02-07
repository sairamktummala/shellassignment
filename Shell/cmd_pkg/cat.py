import sys
def catfun(file):
    data=open(file)
    sys.stdout.write(data.read())
    sys.stdout.write('\n')
def catfun2(cmd):
    content=''
    for i in range(1,len(cmd)):
        data=open(cmd[i])
        content+=(data.read())
    sys.stdout.write(content)
    sys.stdout.write('\n')

