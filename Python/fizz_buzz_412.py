# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
# For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

# 题解：
# 按顺序输出1-n，在3的倍数输出Fizz，在5的倍数输出Buzz，在3，5的公倍数输出FizzBuzz

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        for i in range(1, n+1):
            tem=''
            if i%3==0:
                tem+='Fizz'
            if i%5==0:
                tem+='Buzz'
            if tem=='':
                tem+=str(i)
            result.append(tem)
        return result