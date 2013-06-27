#!/bin/env python
from sys import argv, stdin
if len(argv) < 2:
    input = stdin
else:
    input = open(argv[1])
N,K = [int(x) for x in input.readline().split()]
B = [int(input.readline()) for x in xrange(N)]

profits = [ [0] * (K+1) for _ in xrange(2) ]

prevmax = 0
for i in xrange(1, N + 1):
    board = B[i-1]
    profits[1][0] = prevmax
    for j in xrange(1, K + 1):
        profit = profits[0][j-1] + board
        profits[1][j] = profit
        prevmax = max(profit,prevmax)
    profits.reverse()

print prevmax
