#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        left = 1
        for i in range(1,len(res)):
            res[i] = nums[i-1]*left
            left = res[i]
        right = 1
        for i in range(len(res)-2,-1,-1):
            right *= nums[i + 1]
            res[i] = right*res[i]
        return res
# @lc code=end
# only use output array
# memory left multi res and right multi res
