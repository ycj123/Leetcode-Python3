#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (47.67%)
# Likes:    575
# Dislikes: 0
# Total Accepted:    40.1K
# Total Submissions: 84K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 示例:
# 
# 输入:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        helper = [0]*(n+2)
        res = 0
        for i in range(m):
            stack = []
            for j in range(n):
                if matrix[i][j]=='1':
                    helper[j+1] += 1
                else:
                    helper[j+1] = 0
            for j in range(n+2):
                while stack and helper[j] < helper[stack[-1]]:
                    currheight = helper[stack.pop()]
                    left = stack[-1]
                    right = j-1
                    res = max(res, currheight*(right-left))
                stack.append(j)
        return res

# @lc code=end
# special version of 84
# each row -> Histogram
