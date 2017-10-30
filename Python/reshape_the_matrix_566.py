# In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

# You're given a matrix represented by a two-dimensional array, 
# and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

# Example 1:
# Input: 
# nums = 
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output: 
# [[1,2,3,4]]
# Explanation:
# The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

# Example 2:
# Input: 
# nums = 
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# Output: 
# [[1,2],
#  [3,4]]
# Explanation:
# There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

# Note:
# The height and width of the given matrix is in range [1, 100].
# The given r and c are all positive.
# 题解：
# reshape就是重塑的意思，也就是给定矩阵，然后给定转换的条件，然后重塑矩阵，如果不符合规则的话就输出原有的，符合规则就输出符合规则的矩阵

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # 得到矩阵的行列数
        rows=len(nums)
        cols=len(nums[0])
        
        # 判断行列数是不是和给定的条件是不是一样
        if rows*cols==r*c:
            onedArray=[]
            reshaped=[[0]*c for i in range(r)]
            # 重新塑造矩阵
            for x in nums:
                onedArray+=x
            for index, item in enumerate(onedArray):
                placeRow=index/c
                placeCol=index%c
                reshaped[placeRow][placeCol]=item
            return reshaped
        else:
            return nums