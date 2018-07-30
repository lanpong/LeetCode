# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Note:

# The number of nodes in the given list will be between 1 and 100.

# 题解：就是给定具有头节点的非空单链表，返回链表的中间节点，如果有两个，则返回第二个
# 这时候就需要依次的迭代，一个迭代一次，一个迭代两次，当迭代两次的到null的时候，迭代一次的那个就是中间节点，不需要关注链表是否为奇偶

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head
