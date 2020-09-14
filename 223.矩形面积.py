#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#
# https://leetcode-cn.com/problems/rectangle-area/description/
#
# algorithms
# Medium (43.71%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 27.8K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
# 
# 每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
# 
# 
# 
# 示例:
# 
# 输入: -3, 0, 3, 4, 0, -1, 9, 2
# 输出: 45
# 
# 说明: 假设矩形面积不会超出 int 的范围。
# 
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap
# @lc code=end

