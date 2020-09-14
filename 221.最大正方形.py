#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (42.79%)
# Likes:    553
# Dislikes: 0
# Total Accepted:    71.9K
# Total Submissions: 167.8K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 
# 示例:
# 
# 输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        res_sqrt = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1])+1
                    res_sqrt = max(res_sqrt, dp[i+1][j+1])
        return res_sqrt**2
# @lc code=end
# dynamic programming
