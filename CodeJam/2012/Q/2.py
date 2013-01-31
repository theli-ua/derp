import sys

f = open(sys.argv[1])

casenum = int(f.readline())
def rec(a,b):
    a = str(a)
    b = str(b)
    l = len(a)
    if len(a) != len(b):
        return False
    for i in xrange(len(a)):
        b1 = (b[i:] + b[:i])
        if b1 == a:
            #print a,b,b1
            return True
    return False
#casenum = 1
for casei in xrange(casenum):
    a,b = f.readline().split()
    a = int(a)
    b = int(b)
    res = 0
    for n in xrange(a,b):
        for m in xrange(n+1,b+1):
            if rec(n,m):
                res += 1
    print 'Case #%d: %s' % (casei+1,res)
