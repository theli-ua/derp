class YoungTableau:
    def __init__(self,m,n):
        self.m,self.n = m,n
        self.table = [[None]*m for i in xrange(n)]
    def __str__(self):
        return '\n'.join([str('\t'.join([str(z) for z in x])) for x in self.table])
    def insert(self,x):
        self.table[-1][-1] = x
        self.insert_up(self.m - 1, self.n - 1)
    def extract_min(self):
        m = self.table[0][0]
        self.table[0][0] = None
        self.insert_down(0,0)
        return m
    def insert_down(self,x,y):
        largest = self.table[x][y]
        x2,y2 = x,y
        if x < self.m - 1 and self.table[x+1][y] is not None and (largest is None or self.table[x+1][y] < largest ):
            largest = self.table[x+1][y]
            x2,y2 = x+1,y
        if y < self.n - 1 and self.table[x][y+1] is not None and (largest is None or self.table[x][y+1] < largest ):
            largest = self.table[x][y+1]
            x2,y2 = x,y+1
        if x2 != x or y2 != y:
            self.table[x][y],self.table[x2][y2] = self.table[x2][y2],self.table[x][y]
            self.insert_down(x2, y2)
    def insert_up(self,x,y):
        largest = self.table[x][y]
        x2,y2 = x,y
        if x > 0 and ( self.table[x-1][y] is None or (largest is not None and self.table[x-1][y] > largest )):
            largest = self.table[x-1][y]
            x2,y2 = x-1,y
        if y > 0 and ( self.table[x][y-1] is None or (largest is not None and self.table[x][y-1] > largest )):
            largest = self.table[x][y-1]
            x2,y2 = x,y-1
        if x2 != x or y2 != y:
            self.table[x][y],self.table[x2][y2] = self.table[x2][y2],self.table[x][y]
            self.insert_up(x2, y2)
if __name__ == '__main__':
    x = YoungTableau(4,4)
    testdata = [9,16,3,2,4,8,5,14,12]
    for val in testdata:
        x.insert(val)
    print x
    print x.extract_min()
    print x

    print ''
    x.insert(x.extract_min())
    print x
