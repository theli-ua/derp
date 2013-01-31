#!/usr/bin/python

import sys

f = open(sys.argv[1])

casenum = int(f.readline())
problem = ' welcome to code jam'

for i in xrange(casenum):
	string = f.readline()
	occurences = [0 for x in xrange(len(problem))]
	occurences[0] = 1
	r = range(1,len(problem))
	r.reverse()
	for l in string:
		for x in r:
			if l == problem[x]:
				occurences[x] = (occurences[x] + occurences[x-1]) % 10000
	#print occurences
	
	res = '00000' + str(occurences[-1])
	print 'Case #%d: %s' % (i+1,res[-4:])
	