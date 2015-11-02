
class Node:
    """
    Node class used to find inorder successor of a node
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def inorder_successor(n):
    """
    Given a node n in a binary search tree, explain and code the most 
    efficient way to find the successor of n.

    Solution: there are two cases:
    1. n has a right child: then you just go to the right then keep going left 
    until you hit a leaf
    2. n has a parent: then keep going up until you hit a parent where the child
    is on the left
    """

    if n.right != None:
        currNode = n.right

        # keep going to the left until you hit a leaf
        while currNode.left != None:
            currNode = currNode.left

        return currNode
    else:
        ancestor = n.parent
        child = n

        # keep going up until the child is on the left
        while ancestor != None and child == ancestor.right:
            child = ancestor
            ancestor = child.parent

        return ancestor

