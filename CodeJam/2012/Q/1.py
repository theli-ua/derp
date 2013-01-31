#/usr/bin/python

trans = {'z':'q','q':'z',' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

import sys

f = open(sys.argv[1])

casenum = int(f.readline())

for casei in xrange(casenum):
    temp = f.readline().strip()
    res = ''
    for c in temp:
        res += trans[c]
    print 'Case #%d: %s' % (casei+1,res)
