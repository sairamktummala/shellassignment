import os
import sys
def lessfun(file):
    size=os.popen('stty size','r').read().split()
    rows = int(size[0])
    columns = int(size[1])
    row_count = 0
    column_count = 0
    if os.path.exists(file):
        with open(file) as var:
            for line in var:
                if columns > len(line) and row_count <= rows:
                    sys.stdout.write(line)
                    row_count+=1
                else:
                    x=0
                    y=columns
                    length = len(line)
                    flag = 0 
                    while y <= length and flag == 0 and row_count <= rows:
                        sys.stdout.write(str(line[x:y]))
                        row_count+=1
                        if y == length:
                            flag=1
                        x=y
                        y+=x
                        if y > length:
                            y=length                       
    else:
        sys.stdout.write(file)
        sys.stdout.write(': Doesnot exist')
