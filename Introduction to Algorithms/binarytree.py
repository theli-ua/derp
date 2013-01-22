#/bin/env python

class BinaryTree:
    def __init__(self,key, right=None,left=None):
        self.right = right
        self.left  = left
        self.key = key
    def insert(self, key):
        if key > self.key:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)
        else:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
    def __str__(self,current_depth=0):
        res = '\t'*current_depth + str(self.key)
        if self.left is not None:
            res = '\n'.join([res, self.left.__str__(current_depth + 1)])
        if self.right is not None:
            res = '\n'.join([res, self.right.__str__(current_depth + 1)])
        return res

    def inorder(self):
        if self.left is not None:
            for x in self.left.inorder():
                yield x
        yield self.key
        if self.right is not None:
            for x in self.right.inorder():
                yield x

    def postorder(self):
        if self.right is not None:
            for x in self.right.postorder():
                yield x
        yield self.key
        if self.left is not None:
            for x in self.left.postorder():
                yield x

    def preorder(self):
        yield self.key
        if self.left is not None:
            for x in self.left.preorder():
                yield x
        if self.right is not None:
            for x in self.right.preorder():
                yield x




if __name__ == '__main__':
    bt = BinaryTree(20)
    import random
    for i in xrange(10):
        bt.insert(random.randint(0,50))
    print (bt)


    print ("inorder:")
    inorder = [x for x in bt.inorder()]
    print (inorder)

    print ("postorder:")
    postorder = [x for x in bt.postorder()]
    print (postorder)

    print ("preorder:")
    preorder = [x for x in bt.preorder()]
    print (preorder)
