"""
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，
能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
"""
#  方法一（位运算）：
# class Solution(object):
#     def CheckPermutation(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         if len(s1) != len(s2):
#             return False
#         res = 0
#         for i in range(len(s1)):
#             res += 1 << ord(s1[i])
#             res -= 1 << ord(s2[i])
#         return res == 0
#  方法二：字符串排序后比较
# class Solution(object):
#     def CheckPermutation(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         return sorted(s1) == sorted(s2)

#  方法三：利用集合元素的不可重复性
class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return set(s1) == set(s2)


a = Solution()
# b = a.CheckPermutation('abc', 'bca')
b = a.CheckPermutation('abd', 'bca')
print(b)
"""
思路：位运算
时间复杂度： O(N)
空间复杂度： O(1)
"""