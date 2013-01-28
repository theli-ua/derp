#!/bin/env python
from sys import stdin
#from itertools import chain


N = int(stdin.readline())
casts = []
for _ in xrange(N):
    casts.append( [int(x) for x in stdin.readline().split()] )

casts = sorted(casts)
#print casts

#xxx = max((x for x in chain(*casts)))
#xxx += 1
#_casts = [[] for x in xrange(xxx)]
#for i,c in enumerate(casts):
    #for z in xrange(c[0],c[1] + 1):
        #_casts[z].append(i)
#_casts = [set(x) for x in _casts]

Q = int(stdin.readline())
visits = []
for _ in xrange(Q):
    visits.append([int(x) for x in stdin.readline().split()][1:])

#print (casts)
#print (visits)
from bisect import bisect_left
l = len(casts)
for visit in visits:
    res = set()
    for alien in visit:
        #res |= set([ tuple(x) for x in casts if x[0] <= alien and x[1] >= alien])
        #if alien < xxx:
            #res |= _casts[alien]
        bisection = bisect_left(casts,[alien, alien])
        #print casts[:bisection] , casts[bisection:]
        if bisection < l and casts[bisection][0] <= alien and casts[bisection][1] >= alien:
            res |= set( [tuple(casts[bisection])])
        bisection -= 1
        while bisection >= 0:
            if casts[bisection][1] >= alien:
                res |= set( [tuple(casts[bisection])])
            bisection -= 1

    #print res
        #print bisection
        #print casts[:bisection] , alien ,  casts[bisection:]
    print (len(res))
