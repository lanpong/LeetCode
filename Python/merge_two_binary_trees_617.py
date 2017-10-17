# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.

# Example 1:
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
# Note: The merging process must start from the root nodes of both trees.

# 题解:
# 就是合并两个二叉树，有相同节点的，则相加起来，还放在那个节点，
# 如果一个二叉树的一个节点上有而另一个二叉树的相同节点上没有数据的话就在那个节点上保留有的即可，
# 如此遍历二叉树直至结束

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root=TreeNode(t1.val + t2.val)
            root.left=self.mergeTrees(t1.left, t2.left)
            root.right=self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2
        