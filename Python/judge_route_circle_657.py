# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
# The output should be true or false representing whether the robot makes a circle.

# Example 1:
# Input: "UD"
# Output: true

# Example 2:
# Input: "LL"
# Output: false 
# 题解
# 翻译过来就是给定输入上、下、左、右（R (Right), L (Left), U (Up) and D (down)），然后判断是否回到原点。
# 所以就是很简单的判断输入的R和L、U和D是不是成对出现的，如果是成对出现的就是回到原点了，反之则没有回到。



class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # 参考讨论的得出，直接可以计算LR、UD的出现次数，然后返回就可以了，仅仅需要一行
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
        