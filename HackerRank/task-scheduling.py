#!/bin/python
from bisect import bisect_right

N = int(raw_input())
tasks = []
deadlines = [0] * N
sums = [0] * N
for l in xrange(N):
    x = [int(x) for x in raw_input().split()]
    i = bisect_right(tasks,x)
    tasks.insert(i, x)
    print tasks
    while i <= l:
        if i == 0:
            sums[0] = x[1]
            deadlines[0] = max(0,x[1] - x[0])
        else:
            sums[i] = sums[i-1] + tasks[i][1]
            deadlines[i] = max(deadlines[i-1],sums[i] - tasks[i][0])
        i += 1
    print deadlines[l]

