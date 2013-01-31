#!/usr/bin/python

import sys,re

f = open(sys.argv[1])

temp = f.readline().split()
length = int(temp[0])
wordsc = int(temp[1])
casesc = int(temp[2])
words = []
for i in xrange(wordsc):
	words.append(f.readline().splitlines()[0])
def uniq(seq): 
    # not order preserving 
    set = {} 
    map(set.__setitem__, seq, []) 
    return set.keys()
for i in xrange(casesc):
	case = f.readline().splitlines()[0].replace('(','[').replace(')',']')
	c = re.compile(case)
	result = len([x for x in words if c.match(x)])
	print 'Case #%d: %d' % (i+1,result)
	
		
