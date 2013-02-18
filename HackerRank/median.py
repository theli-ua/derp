#!/bin/python
from bisect import bisect_left
N = int(raw_input())

x = []

for i in range(0, N):
    cmd,num = raw_input().split()
    num = int(num)
    pos = bisect_left(x,num)
    if cmd == 'r':
        if pos >= len(x) or x[pos] != num:
            print 'Wrong!'
            continue
        else:
            del(x[pos])
    else: #a
        x.insert(pos,num)
    l = len(x)
    if l == 0:
        print 'Wrong!'
    elif l & 1:
        print x[l/2]
    else:
        sum = x[l/2] + x[l/2 - 1]
        if sum == 0:
            print sum
        elif sum & 1:
            print float(sum)/2.0
        else:
            print sum/2
