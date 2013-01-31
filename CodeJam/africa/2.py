#!/usr/bin/python

import sys

f = open(sys.argv[1])

count = int(f.readline())

for i in xrange(count):
	words = f.readline().split()
	words.reverse()
	print  'Case #%d: ' % (i+1) + ' '.join(words) 