#!/bin/python
class Treap:
    def __init__(self, x, y, left = None, right = None):
        self.x = x
        self.y = y
        self.Left = left
        self.right = right
    def Merge(L , R):
        if L is None: return R
        if R is None: return L

        if L.y > R.y:
            newR = Treap.Merge(L.Right, R)
            return Treap(L.x, L.y, L.Left, newR)
        else:
            newL = Treap.Merge(L, R.Left)
            return Treap(R.x, R.y, newL, R.Right)

N = int(raw_input())
for l in xrange(N):
    x = [int(x) for x in raw_input().split()]

