#!/usr/bin/python

import sys
from collections import deque

f = open(sys.argv[1])
casenum = int(f.readline())

for casei in xrange(casenum):
	dic_combine = {}
	dic_oppose = {}
	temp = f.readline().split()
	i = 1
	c_count = int(temp[0])
	for _ in xrange(c_count):
		combination = temp[i]
		dic_combine[(combination[0],combination[1])] = combination[2]
		dic_combine[(combination[1],combination[0])] = combination[2]
		i += 1
	op_count = int(temp[i])
	i += 1
	for _ in xrange(op_count):
		opposition = temp[i]
		dic_oppose[opposition[0]] = opposition[1]
		dic_oppose[opposition[1]] = opposition[0]
		i += 1
	
	list_len = int(temp[i])
	i += 1
	l = temp[i]
	i = 1
	res = []
	for i in xrange(list_len):
		#print res,l[i:]
		if len(res) == 0:
			res.append(l[i])
		elif (res[-1],l[i]) in dic_combine:
			res[-1] = dic_combine[(res[-1],l[i])]
		elif l[i] in dic_oppose and dic_oppose[l[i]] in res:
			res = []
		else:
			res.append(l[i])
	print 'Case #%d: [%s]' % (casei+1,', '.join(res))
