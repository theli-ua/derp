#!/usr/bin/python

import sys

def indexof(f, seq):
  for ii,item in enumerate(seq):
    if f(item): 
      return ii

f = open(sys.argv[1])

count = int(f.readline())
mapping = [' ','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
for i in xrange(count):
	message = f.readline()
	last = None
	res = ''
	for letter in message.splitlines()[0]:
		button = indexof(lambda x: letter in x,mapping)
		if button == last:
			res += ' '
		res += ''.join([str(button)]*(1 + mapping[button].index(letter)))
		last = button
	print  'Case #%d: %s' % (i+1,res)
