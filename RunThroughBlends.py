import glob
import os
import time
fnL = glob.glob('*.blend')
for fn in fnL:
    fnew = fn.replace('.blend','')
    #print(fnew)
    os.system("fn='"+fnew+"' blender "+fnew+".blend -P OGN.py")
    #time.sleep(1)
