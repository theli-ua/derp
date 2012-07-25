
class PriorityQueue:
    """just some derp to test mechanics and understanding, no real usage"""
    def __init__(self):
        self.queue = []
    def parent(self,i):
        if i > 0:
            return i/2
        else:
            return None
    def left(self,i):
        i*=2
        i += 1
        if i < len(self.queue):
            return i
        else:
            return None
    def right(self,i):
        i *= 2
        if i < len(self.queue):
            return i
        else:
            return None
    def extract_max(self):
        if len(self.queue) == 0:
            return None
        m = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue = self.queue[:-1]
        self.max_heapify(0)
        return m
    def max_heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if l and self.queue[l] > self.queue[i]:
            largest = l
        else:
            largest = i
        if r and self.queue[r] > self.queue[largest]:
            largest = r
        if largest != i:
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
    x = PriorityQueue()
    from random import randint
    testdata = [randint(-100,100) for _ in range(22)]
    sorteddata = sorted(testdata,cmp=lambda x,y:y-x)
    for i in testdata: 
        x.insert(i)
    testdata = []
    m = x.extract_max()
    while m : 
        testdata.append(m)
        m=x.extract_max()
    print sorteddata
    print testdata

