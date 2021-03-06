#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

# For example, 

# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3

# And the value to search: 2
# You should return this subtree:

#       2     
#      / \   
#     1   3
# In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

# Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.

# 题解:
# 给定二叉搜索树（BST）的根节点和值。 
# 您需要在BST中找到节点的值等于给定值的节点。 
# 返回以该节点为根的子树。 
# 如果此节点不存在，则应返回NULL。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        temp = root
        while temp:
            if temp.val == val:
                return temp
            elif temp.val < val:
                temp = temp.right
            else:
                temp = temp.left