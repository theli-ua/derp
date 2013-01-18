#!/bin/env python
from sys import stdin


T = int(stdin.readline())
for _ in xrange(T):
    nums = sorted([int(x) for x in stdin.readline().split()])
    res = nums[0] * (nums[1] - 1) * (nums[2] - 2) % 1000000007
    print res
