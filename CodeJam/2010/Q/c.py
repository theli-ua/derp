#!/usr/bin/python

import sys
from collections import deque

f = open(sys.argv[1])
casenum = int(f.readline())
def xxx(terms):
	prevx = terms[0]
	res = 1
	
for casei in xrange(casenum):
	temp = f.readline().split()
	R,K,N = (int(x) for x in temp)
	G = deque([int(x) for x in f.readline().split()])
	res = 0
	for _ in xrange(R):
		cur = deque()
		curc = 0
		while len(G) > 0 and (G[0]) <= K-curc:
			curc+=G[0]
			cur.append(G.popleft())
			
		res += curc
		G.extend(cur)
	
	print 'Case #%d: %s' % (casei+1,res)
