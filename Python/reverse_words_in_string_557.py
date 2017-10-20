# Given a string, you need to reverse the order of characters in each word within a sentence while still 
# preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

# 题解：
# 就是反向输出给定的字符串

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([i[::-1] for i in s.split()])