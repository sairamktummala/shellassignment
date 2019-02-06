import sys

 
def wcfun(file):
    countLines = 0
    countWords = 0
    count_char = 0
    with open(file) as var:
        for lines in var:
            count_char += len(lines)
            words=lines.split()
            countLines += 1
            countWords +=len(words)
    sys.stdout.write(str(countLines))
    sys.stdout.write('  ')
    sys.stdout.write(str(countWords))
    sys.stdout.write('  ')
    sys.stdout.write(str(count_char))
    sys.stdout.write('\n')
       
