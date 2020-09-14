#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (40.23%)
# Likes:    750
# Dislikes: 0
# Total Accepted:    85.5K
# Total Submissions: 212.5K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
# 
# 
# 
# 示例 1:
# 
# 输入: [1,2,0]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [3,4,-1,1]
# 输出: 2
# 
# 
# 示例 3:
# 
# 输入: [7,8,9,11,12]
# 输出: 1
# 
# 
# 
# 
# 提示：
# 
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:#empty list
            return 1
        length = len(nums)
        for i in range(length):
            curr = nums[i]#current number
            while 0<curr<length+1 and nums[curr-1]!=nums[i]:#can be index
                nums[i], nums[curr-1] = nums[curr-1], nums[i]
                curr = nums[i]
        for i in range(length):#find the first one not in order
            if i+1 != nums[i]:
                return i+1
        return length + 1 #all is in order
# @lc code=end
#in place hash : index -> value
# 3 4 -1 1
# -1 4 3 1
# -1 1 3 4
# 1 -1 3 4
