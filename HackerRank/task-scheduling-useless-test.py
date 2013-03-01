#!/bin/python
import pydot
def Merge(L , R):
    if L is None: return R
    if R is None: return L

    if L.y > R.y:
        newR = Merge(L.Right, R)
        answer = Treap(L.x, L.y, L.Left, newR)
    else:
        newL = Merge(L, R.Left)
        answer = Treap(R.x, R.y, newL, R.Right)
    answer.Recalc()
    return answer

class Treap:
    def __init__(self, x, y, left = None, right = None):
        self.x = x
        self.y = y
        self.Left = left
        self.Right = right

        self.key = (x,y)
        self.sum = x[0]
        self.deadline = max(0, x[1] - x[0])
    def Recalc(self):

        self.sum = self.x[0]
        if self.Left is not None:
            self.sum += self.Left.sum
        if self.Right is not None:
            self.sum += self.Right.sum

        self.deadline = max(0, self.sum - self.x[0])
        if self.Left is not None:
            self.deadline = max(self.deadline, self.Left.deadline)
        if self.Right is not None:
            self.deadline = max(self.deadline, self.Right.deadline)

    def Split(self, x):
        L = None
        R = None
        newT = None

        if self.x <= x: 
            if self.Right is None:
                R = None
            else:
                newT, R = self.Right.Split(x)
            L = Treap(self.x, self.y, self.Left, newT)
            L.Recalc()
        else:
            if self.Left is None:
                L = None
            else:
                L, newT = self.Left.Split(x)
            R = Treap(self.x, self.y, newT, self.Right)
            R.Recalc()
        return L,R

    def Add(self, x, y):
        l,r = self.Split(x)
        m = Treap(x, y)
        answer = Merge(Merge(l,m), r)
        answer.Recalc()
        return answer

    def dot(self,dot, self_node=None):
        if self_node is None:
            self_node = pydot.Node(str(self.key) + '\t' + str(self.sum))
            dot.add_node(self_node)
        if self.Left:
            left_node = pydot.Node(str(self.Left.key) + '\t' + str(self.Left.sum))
            dot.add_node(left_node)
            dot.add_edge(pydot.Edge(self_node,left_node,label='L'))
            self.Left.dot(dot, self_node = left_node)
        if self.Right:
            right_node = pydot.Node(str(self.Right.key) + '\t' + str(self.Right.sum))
            dot.add_node(right_node)
            dot.add_edge(pydot.Edge(self_node,right_node,label='R'))
            self.Right.dot(dot, self_node = right_node)
    

N = int(raw_input())
tree = None
#N = 2
for l in xrange(N):
    x = [int(x) for x in raw_input().split()]

    if tree is None:
        #tree = Treap(x, l)
        tree = Treap(x, x[0])
    else:
        #tree = tree.Add(x, l)
        tree = tree.Add(x, x[0])
    print tree.deadline
graph = pydot.Dot(graph_type='graph',font='verdana')
tree.dot(graph)
graph.write_png('bt.png')
