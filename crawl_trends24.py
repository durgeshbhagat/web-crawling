import os
import sys
import time
from time import gmtime, strftime

op_dir = 'trends24_india'

from browser import Browser

b = Browser()
link = 'https://trends24.in/india/'
html = b.get_html(link)

try:
    os.mkdir(op_dir)
except:
    print('%s dir exist' %(op_dir))

fname_total ='%s/trends24_india_%s' %(op_dir,strftime("%Y-%m-%d_%H:%M:%S", gmtime()))
print(fname_total)
fout = open(fname_total, 'w')
fout.write(html)
fout.close()
