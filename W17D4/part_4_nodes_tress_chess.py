# Nodes, Trees, and Chess

'''
Nodes and Trees
What is a tree?

A tree is a collection of nodes, each node can have a maximum of one parent.
The node at the top of a tree which has no parent is the root node.
Depending on the type of tree, a node can have multiple children, but in a binary tree it can have a maximum of two.
Nodes with no children are called leaf nodes.
          x
         / \
        x   x
       /   / \
      x   x   x
     /   / \
    x   x   x
'''

'''
Depth first search
First, fully explore the left side of a tree and each subtree
Then move on to the right side.
Traveral order:

          1
         / \
        2   5
       /   / \
      3   6   9
     /   / \
    4   7   8
'''

'''
Breadth first search
First, explore all children of a node.
Then move on to the next level of the tree.
Traveral order:

          1
         / \
        2   3
       /   / \
      4   5   6
     /   / \
    7   8   9
'''

'''
Javascript example

// The start of a node class in JavaScript
class Node {
constructor(value) {
this._value = value;
this._parent = null;
this._children = [];
}
}

const node = new Node("x");
console.log(node)
'''

'''
Chess
What does a knight do?
link to a video describing the knight's moves

https://www.chess.com/lessons/how-to-move-the-pieces/the-knight
'''

'''
Working on Knight Moves
From a given position, the list of possible 
relative moves could be represented by the following:
'''
possible_moves = [ 
    (-2, -1),
    (-2, 1), 
    (-1, -2), 
    (-1, 2), 
    (1, -2), 
    (1, 2), 
    (2, -1), 
    (2, 1),
]

'''
Today’s project
We will be implementing nodes and trees so that we can represent all of the moves
available to a knight as a tree.

Each node will have a value that is a set of coordinates on the board, 
and its children will be the collection of positions a knight at that position could move to.

Here are some additional notes for today’s project:
https://hackmd.io/@jpshafto/S1yh2mmuu
'''