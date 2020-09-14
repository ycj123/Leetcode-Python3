#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (67.52%)
# Likes:    650
# Dislikes: 0
# Total Accepted:    139.3K
# Total Submissions: 206.4K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = grid[0]
        for i in range(1,n):
            res[i] += res[i-1]
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    res[0] += grid[i][j]
                    continue
                res[j] = grid[i][j] + min(res[j], res[j-1])
        return res[-1]

# @lc code=end

