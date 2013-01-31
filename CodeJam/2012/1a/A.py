#!/usr/bin/python

from sys import stdin
from itertools import product

casenum = int(stdin.readline())

def mul(a,b):
    return a*b

for casei in xrange(casenum):
    A,B = [int(x) for x in stdin.readline().split()]
    probabilities = [float(x) for x in stdin.readline().split()]

    #right away
    res = 2 + B

    res = min(B + A + 1.0, res) #retype all

    #now backspacin ...
    for I in xrange(A):
        #how many will I have to retype in case of failure
        #B - A, type to the end
        #2 = 2 enters
        #B - full password
        #I*2 = backspaces+retype backspaced
        false_value = B - A + 2 + B + I*2


        #currently typed characters after backspacing
        a = A - I

        #
        #for i in xrange(a + 1):
            #keep_trying += false_value * reduce(mul, 
                    #[1.0 - x if Xi >= a or Xi == i else x for Xi,x in enumerate(probabilities[:1-I])])
        keep_trying = 0
        print a, probabilities[:a], false_value
        for case in product([False,True], repeat=a):
            case = [c for c in case]
            print case
            if not all(case):
                continue
                keep_trying += (1 + B - A) * \
                    reduce(mul, probabilities)
            else:
                print [x if case[i] else 1.0-x for i,x in enumerate(probabilities[:a])]
                keep_trying += false_value * \
                        reduce(mul, [x if case[i] else 1.0-x for i,x in enumerate(probabilities[:a])])
        res = min(res, keep_trying)
        #all correct



    res = round(res,6)
    print 'Case #%d: %s' % (casei+1,res)
