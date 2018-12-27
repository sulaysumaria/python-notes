import os
import sys

if os.path.isfile('myFile.txt'):

    f = open('myFile.txt', 'r')

    s = f.read()

    print(s)

    f.close()
else:
    print('File does not exist.')
    sys.exit()
