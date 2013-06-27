#!/bin/env python
from sys import argv, stdin
if len(argv) < 2:
    input = stdin
else:
    input = open(argv[1])
N,K = [int(x) for x in input.readline().split()]
B = [int(input.readline()) for x in xrange(N)]

curB = 0
_profit = 0
curMINB = 0
usage = [0] * N
prevLength = 0
debug_colors = ["\033[0m",
    "\033[1m"
]
for i in xrange(len(B)):
    gapPos = i - curB - 1
    if B[i] > 0 and curB < K:
        print '<'
        _profit += B[i]
        usage[i] = 1
        curB += 1
        if B[i] < B[curMINB]:
            curMINB = i
    elif B[i] > B[curMINB]:
        print '2',curMINB, B[curMINB], B[i]
        print prevLength
        newPrevlen = curMINB - (i - curB)
        if newPrevlen + prevLength < K and gapPos >= 0 and B[gapPos] > 0:
            _profit += B[gapPos]
            usage [gapPos] = 1
            prevLength += newPrevlen
        elif prevLength < K and gapPos > 0 and B[gapPos] > B[gapPos - 1]:
            _profit -= B[gapPos - 1]
            _profit += B[gapPos]
            usage [gapPos - 1] = 0
            usage [gapPos ] = 1
            prevLength = newPrevlen + 1
        else:
            prevLength = newPrevlen + 1
        print prevLength
        _profit -= B[curMINB]
        usage[curMINB] = 0
        _profit += B[i]
        usage[i] = 1
        curB = i - curMINB
        curMINB = i - curB + 1
        newMIN = curMINB
        while i >= curMINB:
            if B[newMIN] > B[i]:
                newMIN = i
            i -= 1
        curMINB = newMIN
    elif gapPos > 1 and B[gapPos] + B[i] > B[gapPos-1] + B[i -1]:
        usage[i] = 1
        usage[gapPos] = 1
        usage[i - 1] = 0
        usage[gapPos - 1] = 0

        _profit -= B[i - 1] + B[gapPos - 1]
        _profit += B[i] + B[gapPos]
        gapPos = i - 1
        prevLength = curB
        curMINB = i
        curB = 1
    else:
        print 'else'
        prevLength = curB
        curB = 0
        curMINB = i + 1
    print ', '.join(map(lambda x: debug_colors[usage[x]] + str(B[x]), range(N)))
    print ''
print _profit

