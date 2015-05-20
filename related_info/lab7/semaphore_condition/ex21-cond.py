#!/usr/bin/env python
# coding: utf-8

__author__ = 'Pei Zhongyu'
__version__ = 'Condition'
__number__ = '21'

import threading
import time
import random

N = 16
M = 4 

cond_pair = threading.Condition()
pair = 0
cond_guard = threading.Condition()
guard = M
cond_teacher = threading.Condition()
teacher = 2 

class Student(threading.Thread):
    def __init__(self, stu_name):
        threading.Thread.__init__(self, name=stu_name)
        self.test_time = random.randrange(1,3)

    def run(self):
        global cond_pair, pair, cond_guard, guard, cond_teacher, teacher
        print '[%s] coming.' % self.getName()
        cond_pair.acquire()
        pair += 1
        if pair % 2 == 1:
            cond_pair.wait()
        else:
            cond_pair.notify()
        print '[%s] find the partner.' % self.getName()
        cond_pair.release()

        cond_guard.acquire()
        while guard <= 0:
            cond_guard.wait()
        guard -= 1
        print '[%s] enter room.' % self.getName()
        cond_guard.release()

        cond_teacher.acquire()
        while teacher <= 0:
            cond_teacher.wait()
        teacher -= 1
        print '[%s] teacher checking.' % self.getName()
        time.sleep(self.test_time)
        teacher += 1
        cond_teacher.notify()
        cond_teacher.release()

        cond_guard.acquire()
        print '[%s] Done, exit.' % self.getName()
        guard += 1
        cond_guard.notify()
        cond_guard.release()

print 'N=%d' % N
print 'M=%d' % M
stus = []
for i in range(N):
    stus.append(Student(str(i)))
for t in stus:
    t.start()
