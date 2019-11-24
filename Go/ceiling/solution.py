import sys
import itertools
import math
import string

def printtree(tree):
    act = ''
    if tree['l']!=None:
        printtree(tree['l'])
        act += '('+printtree(tree['l'])+')'
    if tree['r']!=None:
        act += '['+printtree(tree['r'])+']'
    return act

def traverse(tree,val):
    if val<tree['root']:
        if tree['l']==None:
            newtree = {}
            newtree['root']=val
            newtree['l']=None
            newtree['r']=None
            tree['l']=newtree
        else:
            tree['l'] = traverse(tree['l'],val)
    else:
        if tree['r']==None:
            newtree = {}
            newtree['root']=val
            newtree['l']=None
            newtree['r']=None
            tree['r']=newtree
        else:
            tree['r'] = traverse(tree['r'],val)
    return tree

data = sys.stdin.readlines()[1:]
tree_set = set()
for line in data:
    vals = [int(x) for x in line.split()]
    tree = {'root':None}
    for val in vals:
        if tree['root']==None:
            tree['root']=val
            tree['l']=None
            tree['r']=None
        else:
            tree = traverse(tree,val)
    tree_set.add(printtree(tree))
print(len(tree_set))
    