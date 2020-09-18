#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (57.72%)
# Likes:    593
# Dislikes: 0
# Total Accepted:    86.9K
# Total Submissions: 150.3K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 
# 示例 1:
# 
# 输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4.
# 
# 示例 2:
# 
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
# 
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        while len(dp)<=n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5 + 1)))+1,
        return dp[-1]
        

# @lc code=end
# dynamic planning
# minus a square number
