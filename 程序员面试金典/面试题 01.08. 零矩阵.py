"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""
#  方法一：
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix) * [0], len(matrix[0]) * [0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0
#  方法二：
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row, col = len(matrix), len(matrix[0])
        stack = []  #stack来保存元素为0的下标
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    stack.append((i, j))  #遍历一遍矩阵，将元素为0的元素下标存入栈中
        while stack:  #遍历栈中下标组合，分别将对应的行和列置为0即可
            i, j = stack.pop()
            for k in range(col):
                matrix[i][k] = 0
            for k in range(row):
                matrix[k][j] = 0


matrix1 = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
matrix2 = [
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5]
]

a = Solution()
b = a.setZeroes(matrix2)
print(b)

'''
方法一：
解题思路
第一次遍历，用两个数组记录哪一行或者哪一列有0。
第二次遍历，若行i或列j有个元素为0，则将当前元素置0.
方法二：
解题思路
step1:定义一个栈 stack来保存元素为0的下标
step2:遍历一遍矩阵，将元素为0的元素下标存入栈中
step3:遍历栈中下标组合，分别将对应的行和列置为0即可
'''