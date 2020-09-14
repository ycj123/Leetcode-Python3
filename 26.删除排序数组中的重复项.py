#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre = 0
        curr = 1
        length = len(nums)
        if length<2:
            return length
        while curr<length:
            if nums[curr]==nums[curr-1]:
                curr+=1
            else:
                pre +=1
                nums[pre] = nums[curr]
                curr+=1
        return pre+1
# @lc code=end

