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
                if columns > len(line):
                    sys.stdout.write(line)
                else:
                    while columns <= len(line):
                        columns+=columns
                        sys.stdout.write('writing from else')
                        sys.stdout.write(str(line[:columns]))
                        
                        
    else:
        sys.stdout.write(file)
        sys.stdout.write(': Doesnot exist')
