#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_list = []
        col_list = []
        row_l = len(matrix)
        col_l = len(matrix[0])
        for i in range(row_l):
            for j in range(col_l):
                if matrix[i][j] == 0:
                    row_list.append(i)
                    col_list.append(j)
        for i in row_list:
            for j in range(col_l):
                matrix[i][j] = 0
        for i in range(row_l):
            for j in col_list:
                matrix[i][j] = 0
    
# @lc code=end

