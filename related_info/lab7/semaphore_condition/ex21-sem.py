#!/usr/bin/env python
# coding: utf-8

__author__ = 'Pei Zhongyu'
__version__ = 'Semaphore'
__number__ = '21'

import threading
import random
import time

class StuThread(threading.Thread):
    
    pair_num = 0

    def __init__(self, thread_name, teacher, guard, pair):
        threading.Thread.__init__(self, name=thread_name)
        self.teacher = teacher
        self.guard = guard
        self.pair = pair
        self.test_time = random.randrange(1,3)

    def run(self):
        ''' go into room, test, and exit '''
        print '[%s] coming.' % self.getName()
        self.pair.acquire()
        StuThread.pair_num += 1
        self.pair.release()
        time.sleep(random.randint(0,2))
        while StuThread.pair_num % 2 == 1:
            pass
        print '[%s] find the partner.' % self.getName()
        self.guard.acquire()
        print '[%s] enter room.' % self.getName()
        time.sleep(random.randint(0,2))
        self.teacher.acquire()
        print '[%s] teacher checking.' % self.getName()
        time.sleep(self.test_time)
        print '[%s] Done, exit.' % self.getName()
        self.teacher.release()
        self.guard.release()
        
#stu number
N = 12   
#computer number
M = 4    

print 'N=%d' % N
print 'M=%d' % M
random.seed(5)
pair = threading.Semaphore(1)
teacher = threading.Semaphore(2)
guard = threading.Semaphore(M)
threads = []
for i in range(N):
    threads.append(StuThread(str(i), teacher, guard, pair))
for t in threads:
    t.start()
