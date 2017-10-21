# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".
# 反转字符串，切片即可，


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        