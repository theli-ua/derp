#!/usr/bin/python
from sys import stdin
from pprint import pprint

def descend(roots,tree):

    pass

def make_directed(root,tree,depth = 0,depths = None):
    #print s, tree
    for child in tree[root]:
        #print child
        tree[child] -= set([root])
        if depths is not None:
            depths[child] = depth + 1
        #print tree[child]
        make_directed(child,tree, depth + 1, depths)

def protectable(tree,s,tosave):
    if s in tosave:return False
    
    data= ([protectable(tree,child,tosave) \
            for child in tree[s]])
    if len(data) == 0:return True
    return any(data)

T = int(stdin.readline())
for _ in range(T):
    try:
        n,s,t = (int(x) for x in stdin.readline().split())
    except:
        n,s,t = (int(x) for x in stdin.readline().split())
    #print n,s,t
    s -= 1
    tree = []
    for i in range(n):
        data = [int(x) for x in stdin.readline().split()]
        tree.append(set([ x - 1 for x in data[1:]]))
    tosave = set([int(x)-1 for x in stdin.readline().split()])

    #print tree
    make_directed(s,tree)

    if protectable(tree,s,tosave):
        print ('yes')
    else:
        print ('no')

    if False:
        #pprint (tree)
        depths = [0] * n
        directed = list(tree)
        make_directed(s,directed,0,depths)
        #pprint (directed)
        i = 0
        while i < t:
            intersection = directed[i] & tosave
            if len(intersection) > 1:
                tosave -= intersection
                tosave |= set([i])
                i = 0
            else:
                i += 1
        if s in tosave:
            print ('no')
        else:
            #print tosave
            #pprint(depths)
            #print
            savedepths = [depths[x] for x in tosave]
            if len(savedepths) == len(set(savedepths)):
                print ('yes')
            else:
                print ('no')
