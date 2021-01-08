"""
URL化。编写一种方法，将字符串中的空格全部替换为%20。
假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。

示例 1：

输入："Mr John Smith    ", 13
输出："Mr%20John%20Smith"
示例 2：

输入："               ", 5
输出："%20%20%20%20%20"
"""
#  方法一：调用库函数
class Solution(object):
    def replaceSpaces(self, S, length):
        """
        :type S: str
        :type length: int
        :rtype: str
        """
        return S[:length].replace(' ', '%20')
#  方法二：单纯耿直的循环替换
class Solution(object):
    def replaceSpaces(self, S, length):
        """
        :type S: str
        :type length: int
        :rtype: str
        """
        URL = []
        for char in S[:length]:
            if char == ' ':
                URL.append('%20')
            else:
                URL.append(char)
        return ''.join(URL)
