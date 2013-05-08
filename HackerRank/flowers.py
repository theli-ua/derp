#!/bin/python





# code snippet illustrating input/output methods 
N, K = raw_input().split()
N = int(N)
K = int(K)
C = [int(x) for x in raw_input().split()]

HANDS = [[] for _ in xrange(K)]
curK = 0
for _ in xrange(N):
    i = C.index(min(C))
    HANDS[curK].append(C[i])
    del C[i]
    curK = (1 + curK) % K

for i in xrange(K):
    HANDS[i].sort(reverse = True)

result = 0

for h in HANDS:
    for i in xrange(len(h)):
        result += (i+1)*h[i]

print result
