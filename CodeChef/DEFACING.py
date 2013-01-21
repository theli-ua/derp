#!/usr/bin/python
from sys import stdin
from itertools import product


#CONVERSIONS = \
#{'0': ['0', '1', '7'],
 #'1': ['1'],
 #'2': ['2'],
 #'3': ['1', '3', '7'],
 #'4': ['1', '4'],
 #'5': ['5'],
 #'6': ['5', '6'],
 #'7': ['1', '7'],
 #'8': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
 #'9': ['1', '3', '4', '5', '7', '9']}
CONVERSIONS = \
{'0': ['0', '8'],
 '1': ['1', '0', '3', '4', '7', '9', '8'],
 '2': ['2', '8'],
 '3': ['3', '9', '8'],
 '4': ['4', '9', '8'],
 '5': ['5', '6', '9', '8'],
 '6': ['6', '8'],
 '7': ['0', '3', '7', '9', '8'],
 '8': ['8'],
 '9': ['9', '8']}
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
T = int(stdin.readline())
for _ in xrange(T):
    S,M = (x for x in stdin.readline().split())
    
    #possibilities = [ ''.join(y) for y in product ( *(CONVERSIONS[x] for x in S))]
    #print possibilities
    iM = int(M)
    iS = int(S)
    variants = []
    for i in xrange( 1 + len(M) - len(S) ):
        cur = []
        for x in xrange(len(M)):
            if x < i or x >= len(S) + i:
                _from = digits
            else:
                #print S, x - i
                _from = CONVERSIONS[ S[x - i] ]
            c = M[:1 + x]
            print c, _from
            if x > 0:
                cur = product(cur, _from)
            else:
                cur = _from
            cur = [x for x in cur]
            print '\t', [''.join(t) for t in cur]
            for z in cur: print z, ''.join(z) <=c
            cur = [''.join(t) for t in cur if t <= c]
            print '\t\t',[c for c in cur]
            if len(cur) == 0 :break
        variants.append(cur)
    print variants
    #variants = [ int(x) for x in variants if len(x) > 0 ]
    #print ( max ( variants) )
    break
            
