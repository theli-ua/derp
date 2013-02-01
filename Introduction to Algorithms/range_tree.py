#!/bin/env python
from rbtree import RBTree

class RangeTree (RBTree):
    def __init__(self,key):
        RBTree.__init__(self, key)
        self.emax = key[1]

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


    def dot(self,dot, self_node=None):
        if self_node is None:
            if self.isBlack:
                color = 'grey'
            else:
                color = 'red'
            self_node = pydot.Node(str(self.key) + ' ' + str(self.emax), style="filled", fillcolor=color)
            dot.add_node(self_node)
        if self.left:
            if self.left.isBlack:
                color = 'grey'
            else:
                color = 'red'
            left_node = pydot.Node(str(self.left.key) + ' ' + str(self.left.emax), style="filled", fillcolor=color)
            dot.add_node(left_node)
            dot.add_edge(pydot.Edge(self_node,left_node,label='L'))
            self.left.dot(dot, self_node = left_node)
        if self.right:
            if self.right.isBlack:
                color = 'grey'
            else:
                color = 'red'
            right_node = pydot.Node(str(self.right.key) + ' ' + str(self.right.emax), style="filled", fillcolor=color)
            dot.add_node(right_node)
            dot.add_edge(pydot.Edge(self_node,right_node,label='R'))
            self.right.dot(dot, self_node = right_node)

    def find_overlapping(self, Range):
        if Range[0] <= self.key[1] and Range[1] >= self.key[0]:
            return self
        if self.left is not None and self.left.emax >= Range[0]:
            return self.left.find_overlapping(Range)
        elif self.right is not None:
            return self.right.find_overlapping(Range)
        return None



if __name__ == '__main__':
    bt = RangeTree((20,22))
    import random
    for i in xrange(10):
        x = random.randint(0,5000)
        y = random.randint(x,5001)
        #x = i
        #print ('inserting {0}'.format(x))
        bt = bt.insert((x,y))
        #print bt
        #print ('________________________')
    print bt

    if False:
        import pydot
        graph = pydot.Dot(graph_type='graph',font='verdana')
        bt.dot(graph)
        graph.write_png('bt.png')

    print bt.find_overlapping((21,21))
