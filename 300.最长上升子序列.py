#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        helper = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>helper[-1]:
                helper.append(nums[i])
            else:
                left = 0
                right = len(helper) - 1
                while left < right:
                    mid = (left+right)//2
                    if helper[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                helper[left] = nums[i]
        return len(helper) 
# @lc code=end

