#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (40.26%)
# Likes:    741
# Dislikes: 0
# Total Accepted:    91.8K
# Total Submissions: 228.1K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            reverse[i] *= reverse[i-1] or 1
        return max(nums+reverse)
# @lc code=end
# 当负数个数为偶数时候，全部相乘一定最大
# 当负数个数为奇数时候，它的左右两边的负数个数一定为偶数，只需求两边最大值
# 当有 0 情况，重置就可以了

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums: return 
#         res = nums[0]
#         pre_max = nums[0]
#         pre_min = nums[0]
#         for num in nums[1:]:
#             cur_max = max(pre_max * num, pre_min * num, num)
#             cur_min = min(pre_max * num, pre_min * num, num)
#             res = max(res, cur_max)
#             pre_max = cur_max
#             pre_min = cur_min
#         return res