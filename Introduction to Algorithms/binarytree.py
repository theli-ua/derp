#/bin/env python

class BinaryTree:
    def __init__(self,key, right=None,left=None):
        self.right = right
        self.left  = left
        self.key = key
        self.parent = None
    def insert(self, key):
        if self.search(key) is not None:
            return
        if key > self.key:
            if self.right is None:
                self.right = BinaryTree(key)
                self.right.parent = self
            else:
                self.right.insert(key)
        else:
            if self.left is None:
                self.left = BinaryTree(key)
                self.left.parent = self
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

    def min(self):
        if self.left is None:
            return self
        else:
            return self.left.min()

    def max(self):
        if self.right is None:
            return self
        else:
            return self.right.max()

    def next(self):
        if self.right is not None:
            return self.right.min()
        p = self.parent
        x = self
        while p is not None and p.right == x:
            x = p
            p = p.parent
        return p

    def prev(self):
        if self.left is not None:
            return self.left.max()
        p = self.parent
        x = self
        while p is not None and p.left == x:
            x = p
            p = p.parent
        return p
    
    def root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.root()

    def delete(self):
        #will return root of new tree
        root = self.root()
        if self.left is None or self.right is None:
            y = self
        else:
            y = self.next()
        if y.left is not None:
            x = y.left
        else:
            x = y.right
        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            root = x
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        if y != self:
            self.key = y.key
        return root
                

if __name__ == '__main__':
    bt = BinaryTree(20)
    import random
    if True:
        for i in xrange(10):
            bt.insert(random.randint(0,50))
    else:
        for i in [20, 14, 11, 2, 1, 48, 30, 22, 22, 21]:
            bt.insert(i)
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

    print "searching {0}".format(inorder[0])
    print ( bt.search(inorder[0]))
    print "searching {0}".format(inorder[-1])
    print ( bt.search(inorder[-1]))
    print "searching {0}".format(inorder[5])
    print ( bt.search(inorder[5]))
    print ("searching -1")
    print ( bt.search(-1))

    print ()

    print "min : \n" , bt.min()
    print "max : \n" , bt.max()
    print "next({0}) : \n".format(inorder[6]) , bt.search(inorder[6]).next()
    print "prev({0}) : \n".format(inorder[4]) , bt.search(inorder[4]).prev()


    print ()
    to_delete = inorder[4]
    to_delete = 20
    print("deleting {0}\n".format(to_delete))
    bt = bt.search(to_delete).delete()
    print( bt )


    print ("inorder:")
    inorder = [x for x in bt.inorder()]
    print (inorder)

    print ("postorder:")
    postorder = [x for x in bt.postorder()]
    print (postorder)

    print ("preorder:")
    preorder = [x for x in bt.preorder()]
    print (preorder)

    print "searching {0}".format(inorder[0])
    print ( bt.search(inorder[0]))
    print "searching {0}".format(inorder[-1])
    print ( bt.search(inorder[-1]))
    print "searching {0}".format(inorder[5])
    print ( bt.search(inorder[5]))
    print ("searching -1")
    print ( bt.search(-1))

    print ()

    print "min : \n" , bt.min()
    print "max : \n" , bt.max()
    print "next({0}) : \n".format(inorder[6]) , bt.search(inorder[6]).next()
    print "prev({0}) : \n".format(inorder[4]) , bt.search(inorder[4]).prev()


