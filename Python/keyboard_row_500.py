# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


# American keyboard


# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

# 题解：
# 翻译过来就是输入一组单词，返回满足要求的单词
# 要求就是，单词的每一个字母都是必须在美式键盘上的一行上{qwertyuiop}、{asdfghjkl}、{zxcvbnm}，
# 也就是每一个字母都必须在这三个集合中的其中一个，仅仅其中一个，使用正则匹配的话会很简答+过滤器

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
        
    def findWords2(self, words):
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ret = []
        # 使用集合+循环，慢慢匹配，然后返回
        for word in words:
            w = set(word.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
                ret.append(word)
        return ret