# Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
# say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Example 1:
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].

# 题解：
# 翻译过来就是输入 2n 个整数，然后分成n组，第1组则是全部数中最小的两个，第二组是2n-2 数中最小的两个，依次直至全部结束，然后求出每组中最小的那个，最小的相加输出即可
# python中有自带的 sort 排序函数，排一下序每次选出最小的相加即可，也就是每两位选出一个即可，使用切片
# 可以用到的自带函数 sort、sum、

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
        