# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:

# Input: [0,1,0]
# Output: 1
# Example 2:

# Input: [0,2,1,0]
# Output: 1
# Note:

# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above

# 题解：给定已经声明的数组A，并符合一定的条件，A.length >= 3，并且存在这样的 0<i<A.length-1
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# 求出给定数组的 i 即可

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A) - 1
        peak = 0
        
        while low <= high:
            mid = low + (high - low)/2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                peak = mid
                break
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
                
        return peak