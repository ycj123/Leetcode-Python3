#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = left + (right-left)//2
            b = nums[right]
            c = nums[mid]
            if c>b:#not in left
                left = mid+1
            else:#in left
                right = mid
        return nums[left]
# @lc code=end

