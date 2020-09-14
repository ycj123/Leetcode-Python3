#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.37%)
# Likes:    435
# Dislikes: 0
# Total Accepted:    86.6K
# Total Submissions: 195.3K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续
# 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
# 
# 
# 
# 示例：
# 
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 
# 
# 
# 
# 进阶：
# 
# 
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
# 
# 
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        sum_ = 0
        res = len(nums)+1
        for right in range(len(nums)):
            sum_ += nums[right]
            while sum_>=s:
                sum_ -= nums[left]
                res = min(right-left+1, res)
                left += 1
        return res if res!=len(nums)+1 else 0
# @lc code=end
# slide window
