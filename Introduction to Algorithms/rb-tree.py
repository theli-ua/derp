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
        else:
            print 'asdfasdf'
            self.parent.isBlack = True
            return self.root()


    def insert(self,key):
        if self.search(key) is not None:
            return self.root()
        if key > self.key:
            if self.right is None:
                self.right = RBTree(key)
                self.right.parent = self
                self.right.isBlack = False
                return self.right.rb_fixup()
            else:
                return self.right.insert(key)
        else:
            if self.left is None:
                self.left = RBTree(key)
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
            self_node = pydot.Node(str(self.key), style="filled", fillcolor=color)
            dot.add_node(self_node)
        if self.left:
            if self.left.isBlack:
                color = 'grey'
            else:
                color = 'red'
            left_node = pydot.Node(str(self.left.key), style="filled", fillcolor=color)
            dot.add_node(left_node)
            dot.add_edge(pydot.Edge(self_node,left_node,label='L'))
            self.left.dot(dot, self_node = left_node)
        if self.right:
            if self.right.isBlack:
                color = 'grey'
            else:
                color = 'red'
            right_node = pydot.Node(str(self.right.key), style="filled", fillcolor=color)
            dot.add_node(right_node)
            dot.add_edge(pydot.Edge(self_node,right_node,label='R'))
            self.right.dot(dot, self_node = right_node)


if __name__ == '__main__':
    bt = RBTree(20)
    import random
    if True:
        for i in xrange(150):
            x = random.randint(0,5000)
            #x = i
            #print ('inserting {0}'.format(x))
            bt = bt.insert(x)
            #print bt
            #print ('________________________')
    else:
        for i in [48, 40]:
            bt = bt.insert(i)
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



    if True:
        import pydot
        graph = pydot.Dot(graph_type='graph',font='verdana')
        bt.dot(graph)
        graph.write_png('bt.png')
