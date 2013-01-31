#!/usr/bin/python

import sys
import pyopencl as cl
import numpy

f = open(sys.argv[1])
casenum = int(f.readline())

aR = numpy.empty(casenum).astype(numpy.uint32)
aK = numpy.empty(casenum).astype(numpy.uint32)
aN = numpy.empty(casenum).astype(numpy.uint32)
Res = numpy.zeros(casenum).astype(numpy.uint64)

pyG = []
aGindexes = numpy.empty(casenum).astype(numpy.uint32)
curGIndex = 0
for casei in xrange(casenum):
	temp = f.readline().split()
	R,K,N = (int(x) for x in temp)
	G = [int(x) for x in f.readline().split()]
	pyG.extend(G)
	
	aR[casei] = R
	aK[casei] = K
	aN[casei] = N
	aGindexes[casei] = curGIndex
	curGIndex += len(G)
aG = numpy.array(pyG)	
pyG = []
ctx = cl.create_some_context(interactive=True)
queue = cl.CommandQueue(ctx)
#queue.set_property(cl.command_queue_properties.OUT_OF_ORDER_EXEC_MODE_ENABLE,True)
mf = cl.mem_flags
r_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=aR)
k_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=aK)
n_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=aN)
g_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=aG)
gi_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=aGindexes)

res_buf = cl.Buffer(ctx, mf.WRITE_ONLY, Res.nbytes)

prg = cl.Program(ctx, """
     __kernel void solve(__global const uint *r,__global const uint *k,
	__global const uint *n,__global const uint *g,__global const uint *gi,
	__global ulong *resArray
    )
    {
	uint loop,curG,gid;
	ulong res;
    gid  = get_global_id(0);
    curG = 0;
    res = 0;
	for(loop=0; loop < r[gid];loop++)
		{
			uint curN = n[gid];
			uint curc = 0;
			while ( 
				(curN > 0) 
				&& 
				((g[gi[gid] + curG]) <= k[gid]-curc)
				)
			{
				curN = curN  - 1;
				curc = curc + g[gi[gid] + curG];
				curG = (curG + 1) % n[gid];
				
			}
			res += curc;
			//if ((curG == 0) && (loop <= (r[gid] - loop)))
			//{
			//	/* cycle */
			//	int cycles = (r[gid] / (loop + 1));
			//	res = res * cycles;
			//	loop = cycles*(loop + 1) - 1;
			//}
			
		}
	resArray[gid] = res;
    }
    """).build()
#print aR,aK,aN,aG,aGindexes,Res	
prg.solve(queue, aR.shape, r_buf, k_buf, n_buf , g_buf , gi_buf, res_buf)
cl.enqueue_read_buffer(queue, res_buf, Res).wait()

for i,r in enumerate(Res):
	print 'Case #%d: %s' % (i+1,r)
#print aR,aK,aN,aG,aGindexes,Res	
