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
{'0': ['8', '0'],
 '1': ['9', '8', '7', '4', '3', '1', '0'],
 '2': ['8', '2'],
 '3': ['9', '8', '3'],
 '4': ['9', '8', '4'],
 '5': ['9', '8', '6', '5'],
 '6': ['8', '6'],
 '7': ['9', '8', '7', '3', '0'],
 '8': ['8'],
 '9': ['9', '8']}

digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

T = int(stdin.readline())
for _ in range(T):
    S,M = (x for x in stdin.readline().split())
    #variants = []
    res = '////////'
    for i in range( 1 + len(M) - len(S) ):
        prefix_equal = ''
        prefix_less  = ''
        for x in range(len(M)):
            if x < i or x >= len(S) + i:
                _from = digits
            else:
                _from = CONVERSIONS[ S[x - i] ]
            c = M[:1 + x]
            try:
                prefix_less = next( \
                        z for z in (''.join(r) for r in product([prefix_equal or 'z'*x,prefix_less or 'z'*x],_from)) if z < c \
                )
            except:
                prefix_less = None
            prefix_equal = c if prefix_equal is not None and c[-1] in _from else None
            if prefix_equal == prefix_less == None: break
        #variants.append(max([prefix_equal,prefix_less]))
        res = max ( [res,prefix_less or '/' , prefix_equal or '/'] )
        #print res,prefix_equal, prefix_less
    #print (int(max(variants)))
    print (int(res))
