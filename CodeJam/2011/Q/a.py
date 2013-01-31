#!/usr/bin/python

import sys
from collections import deque

f = open(sys.argv[1])
casenum = int(f.readline())

for casei in xrange(casenum):
	O = 1
	B = 1
	Od = 0
	Bd = 0
	temp = f.readline().split()
	steps = 0
	i = 1
	for _ in xrange(int(temp[0])):
		bot = temp[i]
		button = int(temp[i+1])
		if bot == 'O':
			#move to button
			delta = abs(button - O)
			#we may be already on our way
			delta -= Od
			if delta < 0 : delta = 0
			#push the button
			delta += 1
			Od = 0
			O = button
			Bd += delta
		else:
			#move to button
			delta = abs(button - B)
			#we may be already on our way
			delta -= Bd
			if delta < 0 : delta = 0
			#push the button
			delta += 1
			Bd = 0
			B = button
			Od += delta
		steps += delta
		i += 2
	print 'Case #%d: %s' % (casei+1,steps)
