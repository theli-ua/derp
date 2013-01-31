#!/usr/bin/python

import sys

f = open(sys.argv[1])

casenum = int(f.readline())
problem = 'welcome to code jam'

def count_seq(welcome, string):
	#print welcome,string
	if len(welcome) == 1:
		return string.count(welcome[0])
	index = 0
	count = 0
	while True:
		try:
			#print string,welcome[0]
			index = string.index(welcome[0],index)
		except:
			break
		index += 1
		count = (count + count_seq(welcome[1:],string[index:])) % 1000
	return count
	

for i in xrange(casenum):
	string = f.readline()
	res ='0000' + str(count_seq(list(problem),list(string)))
	print 'Case #%d: %s' % (i+1,res[-4:])
	