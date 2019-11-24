// Binary Tree in Golang
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// BinaryNode copied from internet
type BinaryNode struct {
	left  *BinaryNode
	right *BinaryNode
	data  int
}

// BinaryTree copied from internet
type BinaryTree struct {
	root *BinaryNode
}

func (t *BinaryTree) insert(data int) *BinaryTree {
	if t.root == nil {
		t.root = &BinaryNode{data: data, left: nil, right: nil}
	} else {
		t.root.insert(data)
	}
	return t
}

func (n *BinaryNode) insert(data int) {
	if n == nil {
		return
	} else if data <= n.data {
		if n.left == nil {
			n.left = &BinaryNode{data: data, left: nil, right: nil}
		} else {
			n.left.insert(data)
		}
	} else {
		if n.right == nil {
			n.right = &BinaryNode{data: data, left: nil, right: nil}
		} else {
			n.right.insert(data)
		}
	}
}

func numbers(s string) []int {
	var n []int
	for _, f := range strings.Fields(s) {
		i, err := strconv.Atoi(f)
		if err == nil {
			n = append(n, i)
		}
	}
	return n
}

func print(w io.Writer, node *BinaryNode, ns int, ch rune) {
	//var tmp string
	if node == nil {
		return
	}

	for i := 0; i < ns; i++ {
		fmt.Fprint(w, " ")
	}
	//tmp += w
	fmt.Fprintf(w, "%c:%v", ch, node.data)
	print(w, node.left, ns+2, 'L')
	print(w, node.right, ns+2, 'R')
	//tmp += w
	// + ':' //fmt.Fprintf(w, "%c:%v\n", ch, 0) //node.data)
	//tmp += print(w, node.left, ns+2, 'L')
	//tmp += print(w, node.right, ns+2, 'R')
	//return tmp
}

func main() {
	//Read input
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)
	var txtlines []string

	for scanner.Scan() {
		txtlines = append(txtlines, scanner.Text())
	}

	for index, eachline := range txtlines {
		if index != 0 {
			tree := &BinaryTree{}
			expenses := numbers(eachline)
			for _, exp := range expenses {
				tree.insert(exp)
			}
			/*tree.insert(100).
			insert(-20).
			insert(-15).
			insert(50).
			insert(60).
			insert(55).
			insert(85).
			insert(15).
			insert(5).
			insert(-10).
			insert(-60).
			insert(-50)*/
			print(os.Stdout, tree.root, 0, 'M')
			fmt.Println()
		}
	}
}

/*

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
*/
