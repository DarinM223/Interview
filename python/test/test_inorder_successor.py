import unittest
import src.inorder_successor as mod
from src.inorder_successor import Node, inorder_successor

class TestInorderSuccessor(unittest.TestCase):
    def testRightChild(self):
        """
        Test input (* indicates the input node):
               15
             /
            5*
          /   \ 
         2     10
              /
            9
          /
        7

        Test output: the node with key 7
        """
        middleNode = Node(5)

        parentNode = Node(15)
        parentNode.left = middleNode
        middleNode.parent = parentNode

        leftNode = Node(2)
        middleNode.left = leftNode
        leftNode.parent = middleNode

        rightNode = Node(10)
        middleNode.right = rightNode
        rightNode.parent = middleNode

        childLeftNode = Node(9)
        rightNode.left = childLeftNode
        childLeftNode.parent = rightNode

        childLeftLeftNode = Node(7)
        childLeftNode.left = childLeftLeftNode
        childLeftLeftNode.parent = childLeftNode

        self.assertEqual(inorder_successor(middleNode), childLeftLeftNode)

    def testParent(self):
        """
        Test input (* indicates the input node):
               10 
              /   \ 
            1       11
              \ 
               2
                \ 
                 5*
               / 
             4
            /
          3
        Test output: the node with key 10
        """
        oneNode, twoNode, threeNode, fourNode, fiveNode = Node(1), Node(2), Node(3), Node(4), Node(5)
        tenNode, elevenNode = Node(10), Node(11)

        tenNode.right = elevenNode
        elevenNode.parent = tenNode

        tenNode.left = oneNode
        oneNode.parent = tenNode

        oneNode.right = twoNode
        twoNode.parent = oneNode

        twoNode.right = fiveNode
        fiveNode.parent = twoNode

        fiveNode.left = fourNode
        fourNode.parent = fiveNode

        fourNode.left = threeNode
        threeNode.parent = fourNode

        self.assertEqual(inorder_successor(fiveNode), tenNode)

