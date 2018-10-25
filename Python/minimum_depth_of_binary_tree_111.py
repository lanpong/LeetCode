# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# 仍旧是求给定二叉树的深度，DFS即可，O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 0 此处超时，计算 self.minDepth 花了大量的时间
        # if self.minDepth(root.left) == 0 or self.minDepth(root.right) == 0:
        #     return self.minDepth(root.left) + self.minDepth(root.right) + 1
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l == 0 or r == 0:
            return l+r+1
        return min(l, r)+1