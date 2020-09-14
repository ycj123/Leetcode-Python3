#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (34.42%)
# Likes:    629
# Dislikes: 0
# Total Accepted:    84.6K
# Total Submissions: 245.9K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length<2:
            return
        right = length-1
        while right > 0 and nums[right]<=nums[right-1]:
            right -= 1
        if right == 0:#descending
            nums[:] = nums[::-1]#reverse
            return
        right -= 1#pointer to small one
        p2 = length-1
        while nums[p2]<=nums[right]:#find the big one
            p2 -= 1
        nums[p2], nums[right] = nums[right], nums[p2]
        for index in range((length-right)//2):#sort
            nums[right+index+1], nums[length-index-1] = nums[length-index-1], nums[right+index+1]
# @lc code=end
# swap small and big -> bigger
# small position as right as possible
# big position as right as possible
# after swap sort nums behind small position
