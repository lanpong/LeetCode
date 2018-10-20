# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

# Note:

# Both of the given trees will have between 1 and 100 nodes.

# 考虑二叉树的所有叶子。 从左到右的顺序，这些叶子的值形成叶子值序列。

# 如果它们的叶值序列相同，则认为两个二叉树是叶子相似的。

# 当且仅当具有头节点root1和root2的两个给定树是叶类似的时，才返回true。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.findleaf(root1) == self.findleaf(root2)
    
    def findleaf(self, root):
        """
        :type root: TreeNode
        :rtype: list
        """
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]
        return self.findleaf(root.left) + self.findleaf(root.right)