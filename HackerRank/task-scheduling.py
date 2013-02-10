#!/bin/python
from bisect import bisect_left

N = int(raw_input())
tasks = []
for _ in xrange(N):
    #tasks.append([int(x) for x in raw_input().split()])
    #tasks = sorted(tasks, key=lambda x:x[0])
    x = [int(x) for x in raw_input().split()]
    tasks.insert(bisect_left(tasks,x), x)
    print tasks
    curtime = 0
    deadlines = 0
    for task in tasks:
        curtime += task[1]
        d = curtime - task[0]
        if d > deadlines:
            deadlines = d
    print deadlines
