#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
        return max(nums)
# @lc code=end
# new start or not
# new start : stay unchanged
# old : ++
