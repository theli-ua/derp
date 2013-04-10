import sys

f = open(sys.argv[1])

casenum = int(f.readline())

for case in xrange(casenum):
    n = int(f.readline())
    X = [int(x) for x in f.readline().split()]
    Y = [int(x) for x in f.readline().split()]
    X = sorted(X, reverse=True)
    Y = sorted(Y)
    v = zip(X,Y)
    res = map(lambda (a,b): a*b, v)
    res = reduce(lambda x,y:x+y, res)
    print 'Case #%d: %d' % (case + 1, res)
