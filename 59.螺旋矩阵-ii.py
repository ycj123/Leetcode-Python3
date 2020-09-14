#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (78.02%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    44.9K
# Total Submissions: 57.6K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 
# 示例:
# 
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[n**2]]
        n = n**2
        while n > 1:
            newline = [[*range((n-len(res)), n)]]
            n -= len(res)
            res[:] = list(zip(*res[::-1]))#right rotate
            res = newline + res
            
        return res
# @lc code=end
#right rotate -> add new line above
