#!/bin/env python
from sys import stdin
#from itertools import chain
class RangeTree:
    def __init__(self,key):
        self.key = key
        self.isBlack = True
        self.emax = key[1]
        self.left = None
        self.right = None
        self.parent = None
    def insert(self,key):
        if self.search(key) is not None:
            return self.root()
        if self.emax < key[1]:
            self.emax = key[1]
        if key > self.key:
            if self.right is None:
                self.right = RangeTree(key)
                self.right.parent = self
                self.right.isBlack = False
                return self.right.rb_fixup()
            else:
                return self.right.insert(key)
        else:
            if self.left is None:
                self.left = RangeTree(key)
                self.left.parent = self
                self.left.isBlack = False
                return self.left.rb_fixup()
            else:
                return self.left.insert(key)
    def left_rotate(self):
        root = self.root()
        if self.right is None:
            return root
        self.right.parent = self.parent
        y = self.right
        if self.parent is not None:
            if self.parent.left == self:
                self.parent.left = y
            else:
                self.parent.right = y
        self.right = y.left
        if self.right:
            self.right.parent = self
        y.left = self
        self.parent = y
        self.emax = self.key[1]
        if self.left is not None:
            self.emax = max(self.left.emax, self.emax)
        if self.right is not None:
            self.emax = max(self.emax, self.right.emax)
        self.parent.emax = max(self.emax, self.parent.key[1])
        if self.parent.right is not None:
            self.parent.emax = max(self.parent.emax, self.parent.right.emax)
        if y.parent is None:
            return y
        else:
            return root
    def right_rotate(self):
        root = self.root()
        if self.left is None:
            return root
        self.left.parent = self.parent
        y = self.left
        if self.parent is not None:
            if self.parent.right == self:
                self.parent.right = y
            else:
                self.parent.left = y
        self.left = y.right
        if self.left:
            self.left.parent = self
        y.right = self
        self.parent = y
        self.emax = self.key[1]
        if self.left is not None:
            self.emax = max(self.left.emax, self.emax)
        if self.right is not None:
            self.emax = max(self.emax, self.right.emax)
        self.parent.emax = max(self.emax, self.parent.key[1])
        if self.parent.left is not None:
            self.parent.emax = max(self.parent.emax, self.parent.left.emax)
        if y.parent is None:
            return y
        else:
            return root
    def root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.root()
    def search(self, key):
        if self.key == key:
            return self
        nextNode = None
        if key > self.key:
            nextNode = self.right
        else:
            nextNode = self.left
        if nextNode is None:
            return None
        else:
            return nextNode.search(key)
    def rb_fixup(self):
        if self.isBlack: 
            return self.root()
        elif self.parent is None:
            self.isBlack = True
            return self
        elif self.parent.isBlack:
            return self.root()

        #if we are here we really need to rebalance a bit :(
        #there are basically 4 cases depending on if node is left to its parent or right 
        # ll,lr,rl,rr ...

        #ll
        if self.parent.left == self and self.parent.parent.left == self.parent:
            self.isBlack = True
            self.parent.parent.right_rotate()
            return self.parent.rb_fixup()
        #rr
        elif self.parent.right == self and self.parent.parent.right == self.parent:
            self.isBlack = True
            self.parent.parent.left_rotate()
            return self.parent.rb_fixup()
        #lr
        elif self.parent.left == self and self.parent.parent.right == self.parent:
            self.parent.isBlack = True
            self.parent.right_rotate()
            self.parent.left_rotate()
            return self.rb_fixup()
        #rl
        elif self.parent.right == self and self.parent.parent.left == self.parent:
            self.parent.isBlack = True
            self.parent.left_rotate()
            self.parent.right_rotate()
            return self.rb_fixup()
    def find_overlapping(self, Range):
        if Range[0] <= self.key[1] and Range[1] >= self.key[0]:
            yield self
        if self.left is not None and self.left.emax >= Range[0]:
            for x in self.left.find_overlapping(Range):
                yield x
        elif self.right is not None and self.right.emax >= Range[0]:
            for x in self.right.find_overlapping(Range):
                yield x


N = int(stdin.readline())
#casts = []
#for _ in xrange(N):
    #casts.append( [int(x) for x in stdin.readline().split()] )

casts = RangeTree( [int(x) for x in stdin.readline().split()] )
for _ in xrange(N-1):
    casts = casts.insert( [int(x) for x in stdin.readline().split()] )

Q = int(stdin.readline())
visits = []
for _ in xrange(Q):
    visits.append([int(x) for x in stdin.readline().split()][1:])

for visit in visits:
    res = set()
    for alien in visit:
        alien = [alien,alien]
        for c in casts.find_overlapping(alien):
            res |= set( [ tuple(c.key) ])
    print (len(res))
