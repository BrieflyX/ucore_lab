# !/usr/bin/env python
# coding: utf-8

from zio import *
import re
import sys

N = 0
M = 0
partner = {} 
teacher = 2 
parts = 0

#target = ('python ex21-cond.py')
target = ('python ex21-sem.py')
io = zio(target, print_write=False, print_read=COLORED(REPR, 'green'), timeout=9999)

N = int(io.readline().split('=')[1].strip())
M = int(io.readline().split('=')[1].strip())
print '[+] M=%d, N=%d' % (M, N)
r = re.compile(r'\[(\d+)\]')

while True:
    try:
        line = io.read_until('.')
    except:
        break
    id = int(r.findall(line)[0])
    if 'coming' in line:
        partner[id] = -1
    if 'find the partner' in line:
        partner[id] = 1
        parts += 1
        #part = int(line.split(' ')[-1].strip())
        #if partner[part] != -1 and partner[part] != id:
        #    print '[*] %d already have partners!'
        #    sys.exit(1)
        #else:
        #    print '[+] %d -> %d' % (id, part)
        #    partner[id] = part
    if 'enter room' in line:
        if partner[id] == -1:
            print '[*] %d has no partners!' % id
        M -= 1
        if M < 0:
            print '[*] Room is full of students!'
            sys.exit(1)
    if 'teacher checking' in line:
        teacher -= 1
        if teacher < 0:
            print '[*] Teacher cannot check over 2 groups!'
            sys.exit(1)
    if 'Done, exit' in line:
        teacher += 1
        M += 1

if parts % 2 == 0:
    print '[*] Check done, no problems.'
else:
    print '[*] Do not appear in pairs!'
