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
            if nums[i]>helper[-1]:#can append
                helper.append(nums[i])
            else:#cannot append -> find right place
                left = 0
                right = len(helper) - 1
                while left < right:
                    mid = (left+right)//2
                    if helper[mid] < nums[i]:#排除
                        left = mid + 1
                    else:
                        right = mid
                helper[left] = nums[i]
        return len(helper) 
# @lc code=end
# 单调栈 + binary search
