#!/usr/bin/python
from sys import stdin

T = int(stdin.readline())
for _ in xrange(T):
    data = [float(x) for x in stdin.readline().split()]
    res = float( max(data) * 2 - sum(data))
    if res < 0:
        print '0.0'
    else:
        print float(res)

