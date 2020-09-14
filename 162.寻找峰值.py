#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left<right:
            mid = left + (right - left)//2
            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right=mid
        return left
# @lc code=end
# binary
# left or right
