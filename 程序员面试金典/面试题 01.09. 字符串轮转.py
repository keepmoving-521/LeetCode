"""
字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成
（比如，waterbottle是erbottlewat旋转后的字符串）。

示例1:

 输入：s1 = "waterbottle", s2 = "erbottlewat"
 输出：True
示例2:

 输入：s1 = "aa", s2 = "aba"
 输出：False
"""
class Solution(object):
    def isFlipedString(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        s3 = s1 + s1
        return s2 in s3
#  简化方法一
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s1 in s2*2


# s1 = "waterbottle"
# s2 = "erbottlewat"
s1 = "aa"
s2 = "aba"
a = Solution()
b = a.isFlipedString(s1, s2)
print(b)
"""
方法一：
倍增s2，若长度相同的情况下，s1一定为s3的一个子串
复杂度分析
时间复杂度：O(N)
空间复杂度：O(N)
"""