#!/usr/bin/python

import sys
f = open(sys.argv[1])
casenum = int(f.readline())

for casei in xrange(casenum):
	res = 0
	_ = f.readline().splitlines()[0].split()
	N,K,B,T = (int(x) for x in _)
	_ = f.readline().splitlines()[0].split()
	X = [int(x) for x in _]
	_ = f.readline().splitlines()[0].split()
	V = [int(x) for x in _]
	if K > 0:
		badducks = 0
		goodducks = 0
		for i in reversed(xrange(N)):
			if (X[i] + V[i]*T)  >= B:
				res += badducks
				goodducks += 1
			else:
				badducks += 1
			if goodducks >= K:
				break
	else:
		goodducks = K
		
	if goodducks < K:
		print 'Case #%d: IMPOSSIBLE' % (casei+1)
	else:
		print 'Case #%d: %s' % (casei+1,res)
