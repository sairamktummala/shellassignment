import os
import sys
import stat
def lsfun():
    filename=os.listdir('.')
    for name in filename:
            if(name.startswith('.')):
                    pass
            else:
                    sys.stdout.write(name)
                    sys.stdout.write('\n')
            """     
            sys.stdout.write(i)
            sys.stdout.write('ended here')
            sys.stdout.write('\n')
            """