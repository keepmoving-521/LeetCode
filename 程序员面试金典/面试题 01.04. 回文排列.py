"""
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
"""
from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = [i for i in Counter(s).values() if i%2==1]
        return len(count) < 2

"""
借助counter直接计数
counter返回的是字典类型，值是出现次数
奇数只有0个或1个可以达到回文效果
"""