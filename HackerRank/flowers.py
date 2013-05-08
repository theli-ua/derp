#!/bin/python
N, K = [int(x) for x in raw_input().split()]
C = reversed(sorted([int(x) for x in raw_input().split()])[:N])

print reduce(lambda x,y: x + (y[0]/K + 1)*y[1], enumerate(C), 0)
