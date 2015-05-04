#!/usr/bin/env python

import os
import re
import sys

if len(sys.argv) < 3:
    print 'Usage : ' + sys.argv[0] + ' dir1 dir2'
    sys.exit(1)
dir1 = sys.argv[1]
dir2 = sys.argv[2]

f = os.popen('diff ' + dir1 + ' ' + dir2 + ' -q -r | grep differ')
p = re.compile(r'Files\s([^\s]*?)\sand\s([^\s]*?)\sdiffer')
for line in f.readlines():
    m = p.findall(line)
    #print m[0][0]+ ' ' + m[0][1]
    filename = m[0][1][m[0][1].rfind('/')+1:len(m[0][1])]
    if filename.endswith('.c') or filename.endswith('.h'):
        os.system('vimdiff ' + m[0][0] + ' ' + m[0][1])
f.close()
