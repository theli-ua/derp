#!/usr/bin/python

from sys import stdin
casenum = int(stdin.readline())

def mul(a,b):
    return a*b

for casei in xrange(casenum):
    A,B = [int(x) for x in stdin.readline().split()]
    probabilities = [float(x) for x in stdin.readline().split()]

    #right away
    res = (2 + B)

    #delete all
    res = min(res, B + A + 1)
    probability_good = reduce(mul, probabilities)

    #deleting
    for i in xrange(A):
        a = A - i
        if i > 0:
            probability_good /= probabilities[-i]
        probability_bad  = 1.0 - probability_good
        average = probability_good * (B - A + 1 + i*2) +\
                probability_bad * (2*B - A + 2 + i*2)
        res = min(res,average)

    #backspaces
    res = round(res,6)
    print 'Case #%d: %s' % (casei+1,res)
