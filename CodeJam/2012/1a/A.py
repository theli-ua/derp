#!/usr/bin/python

from sys import stdin
casenum = int(stdin.readline())

def mul(a,b):
    return a*b

for casei in xrange(casenum):
    A,B = [int(x) for x in stdin.readline().split()]
    probabilities = [float(x) for x in stdin.readline().split()]
    probabilities.insert(0,1.0)

    #right away
    res = (2 + B)

    probability_good = 1.0
    #deleting
    #i - how much left out of typed messages
    for i in xrange(A + 1):
        probability_good *= probabilities[i]
        probability_bad  = 1.0 - probability_good

        penalty_good = (B - i) + 1 + (A - i)
        penalty_bad  = penalty_good + B + 1
        average = probability_good * penalty_good +\
                  probability_bad  * penalty_bad
        res = min(average,res)

    #backspaces
    res = round(res,6)
    print 'Case #%d: %s' % (casei+1,res)
