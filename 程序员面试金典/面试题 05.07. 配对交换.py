"""
配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。

示例1:

 输入：num = 2（或者0b10）
 输出 1 (或者 0b01)
示例2:

 输入：num = 3
 输出：3
"""
class Solution(object):
    def exchangeBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # return ((num & 0xaaaaaaaa) >> 1) ^ ((num & 0x55555555) << 1)
        #  与上面代码写的效果是一样的
        return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)


a = Solution()
b = a.exchangeBits(3)
print(b)
"""
解题思路
关于二进制及位运算：取出特定位置的数字。

可以先操作奇数位，再操作偶数位。

对于奇数位，使用 101010（即 0xAA）作为掩码，提取奇数位，并把它们右移一位；
对于偶数位，使用 010101（即 0x55）作为掩码，提取偶数位，并把它们左移一位。
步骤：

取出偶数位的数字，向右移位1
取出奇数位的数字，向左移位1
求和或者按位异或
"""
