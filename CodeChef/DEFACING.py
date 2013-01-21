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
for _ in range(T):
    S,M = (x for x in stdin.readline().split())
    
    #possibilities = [ ''.join(y) for y in product ( *(CONVERSIONS[x] for x in S))]
    #print possibilities
    iM = int(M)
    iS = int(S)
    variants = []
    for i in range( 1 + len(M) - len(S) ):
        cur = []
        for x in range(len(M)):
            if x < i or x >= len(S) + i:
                _from = digits
            else:
                _from = CONVERSIONS[ S[x - i] ]
            c = M[:1 + x]
            if x > 0:
                cur = product(cur, _from)
            else:
                cur = _from
            cur = [''.join(t) for t in cur if ''.join(t) <= c]
            if len(cur) == 0 :break
            try:
                _cur = [max([f for f in cur if f < c])]
            except:
                _cur = []
            if c in cur:
                _cur.append(c)
            cur = _cur
            if len(cur) == 0 :break
        variants.extend(cur)
    print (int(max(variants)))
