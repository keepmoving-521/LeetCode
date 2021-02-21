"""
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。
请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
#  方法一：用翻转代替旋转
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

#  方法二：使用辅助数组
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # matrix[:] = matrix_new
        matrix = matrix_new
        return matrix


matrix1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
matrix2 = [
  [5, 1, 9, 11],
  [2, 4, 8, 10],
  [13, 3, 6, 7],
  [15, 14, 12, 16]
]
a = Solution()
b = a.rotate(matrix2)
print(b)
"""
方法一：
复杂度分析

时间复杂度：O(N^2)，其中 N 是 matrix 的边长。对于每一次翻转操作，
我们都需要枚举矩阵中一半的元素。

空间复杂度：O(1)。为原地翻转得到的原地旋转。

方法二：
复杂度分析
时间复杂度：O(N^2)，其中 N 是 matrix 的边长。

空间复杂度：O(N^2)。我们需要使用一个和 matrix 大小相同的辅助数组。
"""