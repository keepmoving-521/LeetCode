"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，
则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:

 输入："aabcccccaaa"
 输出："a2b1c5a3"
示例2:

 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
"""
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ''
        a = S[0]
        b = 0
        c = ''
        for i in S:
            if i == a:
                b += 1
            else:
                c += a + str(b)
                b = 1
                a = i
        c += a + str(b)
        return S if len(S) <= len(c) else c


a = Solution()
# b = a.compressString("aabcccccaaa")
b = a.compressString("abbccd")
print(b)
"""
方法一：模拟
思路

字符串压缩的方式就是将连续出现的相同字符按照 字符 + 出现次数 压缩。
如果压缩后的字符串长度变短，则返回压缩后的字符串，否则保留原来的字符串，
所以我们模拟这个过程构建字符串即可。

算法

我们从左往右遍历字符串，用 c记录当前要压缩的字符，b 记录 c出现的次数，
如果当前枚举到的字符 s[i]等于 c ，我们就更新 b 的计数，即 b = b + 1，
否则我们按题目要求将 c 以及 b 更新到答案字符串 c 里，即 c = c + c + b，完成对 c 字符的压缩。
随后更新 c 为 s[i]，c 为 1，表示将压缩的字符更改为 s[i]。

在遍历结束之后，我们就得到了压缩后的字符串 c，并将其长度与原串长度进行比较。
如果长度没有变短，则返回原串，否则返回压缩后的字符串。
"""