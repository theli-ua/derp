#!/bin/env python
from sys import argv, stdin
if len(argv) < 2:
    input = stdin
else:
    input = open(argv[1])
N,K = [int(x) for x in input.readline().split()]
B = [int(input.readline()) for x in xrange(N)]

prev = [ (0,0) ]

prevmax = 0
for i in xrange(1, N + 1):
    board = B[i-1]
    cur = [ (0, prevmax) ] 
    if board != 0:
        for b in prev:
            curlen = b[0] + 1
            value = b[1] + board
            if value > cur[-1][1]:
                if curlen < K:
                    cur.append( ( curlen, value ) )
                prevmax = max(value, prevmax)
    prev = cur

print prevmax
