# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"

# 题解：就是简单的字符串大写转换为小写，使用lower()即可

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()