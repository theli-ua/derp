#!/bin/env python
from sys import stdin


N = int(stdin.readline())
casts = []
for _ in xrange(N):
    casts.append( [int(x) for x in stdin.readline().split()] )

Q = int(stdin.readline())
visits = []
for _ in xrange(Q):
    visits.append([int(x) for x in stdin.readline().split()][1:])

#print (casts)
#print (visits)

for visit in visits:
    res = set()
    for alien in visit:
        res |= set([ tuple(x) for x in casts if x[0] <= alien and x[1] >= alien])
    print (len(res))
