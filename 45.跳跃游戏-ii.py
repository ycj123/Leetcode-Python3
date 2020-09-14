#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (37.44%)
# Likes:    679
# Dislikes: 0
# Total Accepted:    79.2K
# Total Submissions: 211.4K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 
# 示例:
# 
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 
# 
# 说明:
# 
# 假设你总是可以到达数组的最后一个位置。
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 1# next element of current interval
        jump = 0
        start = 0# start of current interval
        while end < len(nums):#end == length : current interval end with target
            currmax = 0
            for i in range(start,end):
                currmax = max(currmax, i+nums[i])
            start = end
            end = currmax+1
            jump += 1
        return jump
# @lc code=end
# store maximum for each interval
# jump to next interval only takes one jump
# O(n)
