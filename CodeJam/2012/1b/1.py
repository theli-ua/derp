
#/usr/bin/python
import sys

f = open(sys.argv[1])

casenum = int(f.readline())

for casei in xrange(casenum):
    temp = f.readline().strip().split(' ')[1:]
    temp = map(int,temp)
    X = sum(temp)
    X2 = float(X*2)
    res = []
    l = len(temp) - 1
    
    for i,J in enumerate(temp):
        other = temp[:i]
        other.extend(temp[i+1:])
        other = sorted(other)
        otherbest = other[-1]
        otherbest = other[0]
        otherworst = other[0]
        # final = J + X*?
        #J1 + X*a - J2 - X*(1.0-a) = 0
        #print otherbest
        #print i,J,otherbest
        p = 100.0*(otherbest - J + X)/X2
        #p2 = 100.0*(otherworst - J )/X2
        res.append(str(round(p,7)))
    print 'Case #%d: %s' % (casei+1,' '.join(res))
