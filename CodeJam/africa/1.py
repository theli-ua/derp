#!/usr/bin/python

import sys

f = open(sys.argv[1])

count = int(f.readline())

for i in xrange(count):
	credit = int(f.readline())
	itemcount = int(f.readline())
	items = [int(x) for x in f.readline().split()]
	ii2 = 0
	res = []
	for x in xrange(itemcount):
		for ii in (zz for zz in xrange(itemcount) if zz != x):
			if items[x] + items[ii] == credit:
				res = [x+1,ii+1]
				break
		if len(res) >0 :
			break
	
	res.sort()
	print 'Case #%d: %d %d' % (i+1,res[0],res[1])
