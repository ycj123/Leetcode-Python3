#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<2:
            return nums[0]
        def helper(hasStart):
            start = 0 if hasStart else 1
            end = len(nums) - 2 + start
            curr = pre = 0
            for n in nums[start:end+1]:
                t = curr
                curr = max(curr, pre+n)
                pre = t
            return curr
        return max(helper(0), helper(1))
            
# @lc code=end

