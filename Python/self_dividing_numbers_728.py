# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Example 1:
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# Note:

# The boundaries of each input argument are 1 <= left <= right <= 10000.

# 题解：给出上限和下限，求得自分割数的个数，自分割数的概念就是：
# 自分割数是一个可被其包含的每个数字整除的数字。 例如，128是自分割数，
# 因为128％1 == 0,128％2 == 0，128％8 == 0.此外，不允许自分割数包含数字零。
# 给定下限和上限数字，输出每个可能的自分割数列表，如果可能，包括边界。

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left, right+1):
            if '0' in str(num):
                continue
            if sum([num % int(digit) for digit in str(num)]) == 0:
                result.append(num)
        return result