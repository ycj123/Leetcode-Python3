#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (52.36%)
# Likes:    1591
# Dislikes: 0
# Total Accepted:    139.8K
# Total Submissions: 266.9K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = [0]*len(height)
        right = [0]*len(height)
        max_i = 0
        for i in range(len(height)):
            left[i] = max_i
            if height[i] > max_i:
                max_i = height[i]
        max_i = 0
        for i in range(len(height)-1,-1,-1):
            right[i] = max_i
            if height[i]>max_i:
                max_i = height[i]
        res = 0
        for i in range(len(height)):
            res += max((min(left[i],right[i]) - height[i]), 0)
        return res
# @lc code=end
# store the left maximum and right maximum
# for each position
