import sys

f = open(sys.argv[1])

casenum = int(f.readline())

for case in xrange(casenum):
	senum = int(f.readline())
	se = []
	for _ in xrange(senum):
		se.append(f.readline().splitlines()[0])
	qnum = int(f.readline())
	q = []
	for _ in xrange(qnum):
		q.append(f.readline().splitlines()[0])
	switches = 0
	while len(q) > 0:
		l = 0
		for s in se:
			try:
				l = max(l,q.index(s))
			except:
				l = len(q)
				break
		if l == len(q):
			break
		else:
			switches += 1
			q = q[l:]
	print 'Case #%d: %d' % (case+1,switches)
