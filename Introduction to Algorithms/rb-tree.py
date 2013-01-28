#!/bin/env python
from binarytree import BinaryTree

class RBTree (BinaryTree):
    def __init__(self,key):
        BinaryTree.__init__(self, key)
        self.isBlack = True
    def __str__(self,current_depth=0):
        res = '\t'*current_depth + str(self.key)
        if self.isBlack: res += '(b)'
        else: res += '(r)'
        if self.left is not None:
            res = '\n'.join([res, self.left.__str__(current_depth + 1)])
        if self.right is not None:
            res = '\n'.join([res, self.right.__str__(current_depth + 1)])
        return res
    def rb_fixup(self):
        return
        if self.isBlack: return
        while self.parent is not None and not self.parent.isBlack:
            if self.parent == self.parent.parent.left:
                y = self.parent.parent.right
                if not y.isBlack:
                    y.parent.isBlack = True
                    y.isBlack = True
                    self.parent.parent.rb_fixup()
                elif self == self.parent.right:
                    self.parent.left_rotate()
                    self.parent.isBlack = True
                    self.parent.parent.isBlack = False
                    self.parent.parent.right_rotate()
            else:
                y = self.parent.parent.left
                if not y.isBlack:
                    y.parent.isBlack = True
                    y.isBlack = True
                    self.parent.parent.rb_fixup()
                elif self == self.parent.left:
                    self.parent.right_rotate()
                    self.parent.isBlack = True
                    self.parent.parent.isBlack = False
                    self.parent.parent.left_rotate()

    def insert(self,key):
        if self.search(key) is not None:
            return
        if key > self.key:
            if self.right is None:
                self.right = RBTree(key)
                self.right.parent = self
                self.right.isBlack = False
                self.right.rb_fixup()
            else:
                self.right.insert(key)
        else:
            if self.left is None:
                self.left = RBTree(key)
                self.left.parent = self
                self.left.isBlack = False
                self.left.rb_fixup()
            else:
                self.left.insert(key)
    def left_rotate(self):
        root = self.root()
        if self.right is None:
            return root
        y = self.right
        self.right = y.left
        y.left = self
        y.parent = self.parent
        self.parent = y
        if y.parent is None:
            return y
    def right_rotate(self):
        root = self.root()
        if self.left is None:
            return root
        y = self.left
        self.left = y.right
        y.right = self
        y.parent = self.parent
        self.parent = y
        if y.parent is None:
            return y



if __name__ == '__main__':
    bt = RBTree(20)
    bt.insert(10)
    bt.insert(30)
    bt.insert(25)
    bt.insert(35)
    print ( bt )
    print ("left rotate 20: ")
    bt = bt.search(20).left_rotate()
    print (bt)
    print ("right rotate 30: ")
    bt = bt.search(30).right_rotate()
    print (bt)
    pass
