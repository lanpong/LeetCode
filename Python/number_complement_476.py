# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.

# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

# 题解：
# 就是求一个正整数的补码，直接使用操作码"<<"和"^" 来进行运算，这俩操作码是直接在二进制上运算的，然后返回的结果还是十进制，所以不用考虑将正整数转化为二进制来进行计算，直接就可以。



class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=1
        while i<=num:
            i=i<<1
        return (i-1)^num
        