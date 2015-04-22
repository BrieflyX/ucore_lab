#! /usr/bin/env python
# coding: utf-8
# authorized by Pei Zhongyu, could be plagiarized cuz I put it on GitHub. 
# may change other place's code, not only comment place

__author__ = 'Pei Zhongyu'

import sys
from optparse import OptionParser
import random

def stride_pass(joblist, quantum=1.0):
    '''
        Stride Algorithm
        Ignoring overflow
    '''
    # set for priority
    BIGSTRIDE = 100
    priority = range(1,len(joblist)+1)
    random.shuffle(priority)
    new_joblist = []
    for job,pr in zip(joblist,priority):
        new_joblist.append((job[0],job[1],0,BIGSTRIDE/pr))
        print 'Job %d : pass=%d' % (job[0],BIGSTRIDE/pr)
    joblist = new_joblist

    print 'Execution trace:'
    turnaround = {}
    response = {}
    lastran = {}
    wait = {}
    jobcount = len(joblist)
    for i in range(jobcount):
        lastran[i] = 0.0
        wait[i] = 0.0
        turnaround[i] = 0.0
        response[i] = -1

    runlist = []
    for e in joblist:
        runlist.append(e)

    thetime  = 0.0
    while jobcount > 0:
        # print '%d jobs remaining' % jobcount
        job = runlist.pop(0)
        jobnum  = job[0]
        runtime = float(job[1])
        stride = job[2]
        pas = job[3]
        if response[jobnum] == -1:
            response[jobnum] = thetime
        currwait = thetime - lastran[jobnum]
        wait[jobnum] += currwait
        ranfor = quantum 
        if runtime > quantum:
            # p z y 
            print '  [ time %3d ] Run job %3d for %.2f secs, stride = %d' % (thetime, jobnum, ranfor, stride)
            runlist.append((jobnum, runtime-ranfor, stride+pas, pas))
        else:
            # pzy
            print '  [ time %3d ] Run job %3d for %.2f secs ( DONE at %.2f )' % (thetime, jobnum, ranfor, thetime + ranfor)
            turnaround[jobnum] = thetime + ranfor
            jobcount -= 1
        thetime += ranfor
        lastran[jobnum] = thetime
        runlist.sort(cmp=lambda x,y:int(x[2]-y[2]))

    print '\nFinal statistics:'
    turnaroundSum = 0.0
    waitSum       = 0.0
    responseSum   = 0.0
    for i in range(0,len(joblist)):
        turnaroundSum += turnaround[i]
        responseSum += response[i]
        waitSum += wait[i]
        print '  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (i, response[i], turnaround[i], wait[i])
    count = len(joblist)
    
    print '\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' % (responseSum/count, turnaroundSum/count, waitSum/count)


if __name__ == '__main__' and __author__ == 'Pei Zhongyu':

    parser = OptionParser()
    parser.add_option("-s", "--seed", default=0, help="the random seed", 
                      action="store", type="int", dest="seed")
    parser.add_option("-j", "--jobs", default=3, help="number of jobs in the system",
                      action="store", type="int", dest="jobs")
    parser.add_option("-l", "--jlist", default="", help="instead of random jobs, provide a comma-separated list of run times",
                      action="store", type="string", dest="jlist")
    parser.add_option("-m", "--maxlen", default=10, help="max length of job",
                      action="store", type="int", dest="maxlen")
    parser.add_option("-p", "--policy", default="FIFO", help="sched policy to use: SJF, FIFO, RR",
                      action="store", type="string", dest="policy")
    parser.add_option("-q", "--quantum", help="length of time slice for RR policy", default=1, 
                      action="store", type="int", dest="quantum")
    parser.add_option("-c", help="compute answers for me", action="store_true", default=True, dest="solve")

    (options, args) = parser.parse_args()

    random.seed(options.seed)

    print 'ARG policy', options.policy
    if options.jlist == '':
        print 'ARG jobs', options.jobs
        print 'ARG maxlen', options.maxlen
        print 'ARG seed', options.seed
    else:
        print 'ARG jlist', options.jlist

    print ''

    print 'Here is the job list, with the run time of each job: '

    import operator

    joblist = []
    if options.jlist == '':
        for jobnum in range(0,options.jobs):
            runtime = int(options.maxlen * random.random()) + 1
            joblist.append([jobnum, runtime])
            print '  Job', jobnum, '( length = ' + str(runtime) + ' )'
    else:
        jobnum = 0
        for runtime in options.jlist.split(','):
            joblist.append([jobnum, float(runtime)])
            jobnum += 1
        for job in joblist:
            print '  Job', job[0], '( length = ' + str(job[1]) + ' )'
    print '\n'

    if options.solve == True:
        print '** Solutions **\n'
        if options.policy == 'SJF':
            # pz y's CODE
            thetime = 0
            joblist.sort(cmp=lambda x,y:int(x[1]-y[1]))

            print 'Execution trace:'
            # p zy
            for job in joblist:
                print '[ time %3d ] Run job %d for %.2f secs (DONE at %.2f )' % (thetime, job[0], job[1], thetime+job[1])
                thetime += job[1]
             
            print '\nFinal statistics:'
            t     = 0.0
            count = 0
            turnaroundSum = 0.0
            waitSum       = 0.0
            responseSum   = 0.0
            for tmp in joblist:
                jobnum  = tmp[0]
                runtime = tmp[1]
                
                response   = t
                turnaround = t + runtime
                wait       = t
                print '  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (jobnum, response, turnaround, wait)
                responseSum   += response
                turnaroundSum += turnaround
                waitSum       += wait
                t += runtime
                count = count + 1
            print '\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' % (responseSum/count, turnaroundSum/count, waitSum/count)
            
        if options.policy == 'FIFO':
            thetime = 0
            print 'Execution trace:'
            # p zy
            for job in joblist:
                print '[ time %3d ] Run job %d for %.2f secs (DONE at %.2f )' % (thetime, job[0], job[1], thetime+job[1])
                thetime += job[1]
             
            print '\nFinal statistics:'
            t     = 0.0
            count = 0
            turnaroundSum = 0.0
            waitSum       = 0.0
            responseSum   = 0.0
            for tmp in joblist:
                jobnum  = tmp[0]
                runtime = tmp[1]
                
                response   = t
                turnaround = t + runtime
                wait       = t
                print '  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (jobnum, response, turnaround, wait)
                responseSum   += response
                turnaroundSum += turnaround
                waitSum       += wait
                t += runtime
                count = count + 1
            print '\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' % (responseSum/count, turnaroundSum/count, waitSum/count)
                         
        if options.policy == 'RR':
            print 'Execution trace:'
            turnaround = {}
            response = {}
            lastran = {}
            wait = {}
            quantum  = float(options.quantum)
            jobcount = len(joblist)
            for i in range(0,jobcount):
                lastran[i] = 0.0
                wait[i] = 0.0
                turnaround[i] = 0.0
                response[i] = -1

            runlist = []
            for e in joblist:
                runlist.append(e)

            thetime  = 0.0
            while jobcount > 0:
                # print '%d jobs remaining' % jobcount
                job = runlist.pop(0)
                jobnum  = job[0]
                runtime = float(job[1])
                if response[jobnum] == -1:
                    response[jobnum] = thetime
                currwait = thetime - lastran[jobnum]
                wait[jobnum] += currwait
                ranfor = quantum 
                if runtime > quantum:
                    # p z y 
                    print '  [ time %3d ] Run job %3d for %.2f secs' % (thetime, jobnum, ranfor)
                    runlist.append([jobnum, runtime-ranfor])
                else:
                    # pzy
                    print '  [ time %3d ] Run job %3d for %.2f secs ( DONE at %.2f )' % (thetime, jobnum, ranfor, thetime + ranfor)
                    turnaround[jobnum] = thetime + ranfor
                    jobcount -= 1
                thetime += ranfor
                lastran[jobnum] = thetime

            print '\nFinal statistics:'
            turnaroundSum = 0.0
            waitSum       = 0.0
            responseSum   = 0.0
            for i in range(0,len(joblist)):
                turnaroundSum += turnaround[i]
                responseSum += response[i]
                waitSum += wait[i]
                print '  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (i, response[i], turnaround[i], wait[i])
            count = len(joblist)
            
            print '\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' % (responseSum/count, turnaroundSum/count, waitSum/count)
        
        if options.policy == 'STRIDE':
            stride_pass(joblist)

        if options.policy != 'FIFO' and options.policy != 'SJF' and options.policy != 'RR' and options.policy != 'STRIDE': 
            print 'Error: Policy', options.policy, 'is not available.'
            sys.exit(0)
    else:
        print 'Compute the turnaround time, response time, and wait time for each job.'
        print 'When you are done, run this program again, with the same arguments,'
        print 'but with -c, which will thus provide you with the answers. You can use'
        print '-s <somenumber> or your own job list (-l 10,15,20 for example)'
        print 'to generate different problems for yourself.'
        print ''

