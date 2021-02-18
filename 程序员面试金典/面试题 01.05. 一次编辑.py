""""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。
给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例 1:
输入:
first = "pale"
second = "ple"
输出: True
 
示例 2:
输入:
first = "pales"
second = "pal"
输出: False
"""
class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        if abs(len(first) - len(second)) > 1:
            return False
        if len(second) - len(first) < 0:
            first, second = second, first
        for i in range(len(first)):
            if first[i] == second[i]:
                continue
            return first[i:] == second[i+1:] or first[i+1:] == second[i+1:]
        return True


"""
要点：
    增删改功能特点就是：自不同位起，后续都一样
易错点：
    比较时，如果第1个字符串比较长，可能会index溢出；
    又因为增和删其实是逆操作，可直接把两个字符串交换
    注意比较改时，是i+1不是i
    因为第2个肯定比第1个长了，所以只存在增和改的比较

"""