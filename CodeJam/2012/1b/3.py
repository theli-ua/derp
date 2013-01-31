#/usr/bin/python
import sys,itertools

f = open(sys.argv[1])

casenum = int(f.readline())

for casei in xrange(casenum):
    temp = f.readline().strip().split(' ')[1:]
    temp = map(int,temp)
    res = ''
    d = {}
    done = False
    for i in xrange(len(temp)):
        for s in itertools.combinations(temp,i+1):
            #print s
            n = sum(s)
            if n in d:
                res = '{0}\n{1}'.format(' '.join(map(str,d[n])),' '.join(map(str,s)))
                done = True
                break
            else:
                d[n] = s
        if done: break
    print 'Case #%d:' % (casei+1)
    if done:print res
    else: print 'Impossible'
    #for c in temp:
        #res += trans[c]
    #print 'Case #%d: %s' % (casei+1,res)
