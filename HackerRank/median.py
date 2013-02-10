#!/bin/python
from bisect import bisect_left


# code snippet for illustrating input/output

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
        print float(x[l/2] + x[l/2 - 1]) / 2.0
