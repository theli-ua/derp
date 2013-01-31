#!/usr/bin/python

import sys
f = open(sys.argv[1])
casenum = int(f.readline())
res = 0
dirs = {}

def mkdir(dir):
	global res
	global dirs
	curdirs = dirs
	for dir in (x for x in dir.split('/') if len(x) > 0):
		#print res,dir,curdirs
		if dir not in curdirs:
			res += 1
			curdirs[dir] = {}
		curdirs = curdirs[dir]
	

for casei in xrange(casenum):
	dirs = {}
	_ = f.readline().splitlines()[0].split()
	N,M = int(_[0]),int(_[1])
	
	for _ in xrange(N):
		mkdir(f.readline().splitlines()[0])
	res = 0
	for _ in xrange(M):
		mkdir(f.readline().splitlines()[0])
	print dirs

	print 'Case #%d: %s' % (casei+1,res)
