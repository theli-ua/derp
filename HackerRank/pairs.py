from sys import stdin
from bisect import bisect_left

N, K = (int(x) for x in stdin.readline().split())
NUMS = [int(x) for x in stdin.readline().split()]

NUMS = sorted(NUMS)
res = 0
for num in NUMS:
    to_find = num+K
    pos = bisect_left(NUMS,to_find)
    if pos < N and NUMS[pos] == to_find:
        res += 1
print res
