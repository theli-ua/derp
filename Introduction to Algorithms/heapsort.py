
class PriorityQueue:
    """just some derp to test mechanics and understanding, no real usage"""
    def __init__(self,d=2):
        self.queue = []
        self.d = d
    def parent(self,i):
        if i >= 0:
            return i/self.d
        else:
            return None
    def childs(self,i):
        for x in xrange(self.d):
            c = i * self.d + x
            if c < len(self.queue):
                yield c
            else:
                yield None
    def extract_max(self):
        if len(self.queue) == 0:
            return None
        m = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue = self.queue[:-1]
        self.max_heapify(0)
        return m
    def max_heapify(self,i):
        childs = [(x,self.queue[x]) for x in self.childs(i) if x is not None]
        childs.sort(cmp = lambda (x,y),(x2,y2): y2 - y)
        if len(childs) >0 and childs[0][1] > self.queue[i]:
            largest = childs[0][0]
            self.queue[i],self.queue[largest] = self.queue[largest],self.queue[i]
            self.max_heapify(largest)
    def increase_key(self,i,value):
        self.queue[i] = value
        while self.parent(i) is not None:
            p = self.parent(i)
            if self.queue[p] < self.queue[i]:
                self.queue[p],self.queue[i] = self.queue[i],self.queue[p]
                i = p
            else:
                break
    def insert(self,key):
        self.queue.append(key)
        self.increase_key(len(self.queue)-1,key)

if __name__ == '__main__':
    x = PriorityQueue(2)
    from random import randint
    testdata = [randint(-100,100) for _ in range(4)]
    sorteddata = sorted(testdata,cmp=lambda x,y:y-x)
    for i in testdata: 
        x.insert(i)
    testdata = []
    print x.queue
    m = x.extract_max()
    while m is not None: 
        testdata.append(m)
        m=x.extract_max()
    print sorteddata
    print testdata

