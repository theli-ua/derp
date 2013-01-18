#!/bin/env python
from sys import stdin
T = int(stdin.readline())
for _ in xrange(T):
    N = int(stdin.readline())
    workers = [int(x) for x in stdin.readline().split()]
    print sum(workers) - N * min(workers)
