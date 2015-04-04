#!/usr/bin/env python

import os
import re

s = raw_input('input 2 directory to merge:')
dir1 = s.split(' ')[0].strip()
dir2 = s.split(' ')[1].strip()

f = os.popen('diff ' + dir1 + ' ' + dir2 + ' -q -r | grep differ')
p = re.compile(r'Files\s([^\s]*?)\sand\s([^\s]*?)\sdiffer')
for line in f.readlines():
    m = p.findall(line)
    #print m[0][0]+ ' ' + m[0][1]
    os.system('vimdiff ' + m[0][0] + ' ' + m[0][1])
f.close()
