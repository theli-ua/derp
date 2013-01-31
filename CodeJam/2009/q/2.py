#!/usr/bin/python

import sys

f = open(sys.argv[1])

casenum = int(f.readline())
def get_sink(x,y,w,h,map):
	sink = (x,y)
	for ceil in [ceil for ceil in [(x,y-1),(x-1,y),(x+1,y),(x,y+1)] if (0 <= ceil[0] and ceil[0] < w) and (0 <= ceil[1] and ceil[1] < h)]:
		if map[ceil[1]][ceil[0]] < map[sink[1]][sink[0]]:
			sink = ceil
	return sink
for casei in xrange(casenum):
	temp = f.readline().split()
	h = int(temp[0])
	w = int(temp[1])
	map = []
	for i in xrange(h):
		map.append([int(x) for x in f.readline().split()])
	basin = ord('a')
	resmap = []
	for i in xrange(h):
		resmap.append([None] * w)
	for y in xrange(h):
		for x in xrange(w):
			if resmap[y][x] == None:
				sink = get_sink(x,y,w,h,map)
				if sink == (x,y):
					resmap[y][x] = chr(basin)
					basin +=1
				else:
					prevsink = (x,y)
					path = [prevsink]					
					while (resmap[sink[1]][sink[0]]) == None and prevsink != sink:
						path.append(sink)
						prevsink = sink
						sink = get_sink(sink[0],sink[1],w,h,map)
					if resmap[sink[1]][sink[0]] == None:
						for step in path:
							resmap[step[1]][step[0]] = chr(basin)
						basin += 1
					else:
						resmap[y][x] = resmap[sink[1]][sink[0]]
	print 'Case #%d:' % (casei+1)
	for row in resmap:
		print ' '.join(row)
				
	
	

		
