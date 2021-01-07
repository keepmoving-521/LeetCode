"""
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false
示例 2：

输入: s = "abc"
输出: true
"""
class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        astr_set = set(astr)
        if len(astr) == len(astr_set):
            return True
        else:
            return False
"""
解题思路
将字符串转化为列表
将字符串用内置函数 set() 转换为集合，此时集合会自动排除重复项。
之后将列表转化为集合，利用集合元素的不可重复性进行长度判断，
如果有重复元素，则会进行去重，长度改变
"""