#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper  = {} # hashmap to store pre numbers
        for index,num in enumerate(nums):
            aim = target - num
            if aim in helper:
                return [helper[aim], index]
            helper[num] = index
        return False
# @lc code=end
#O(n)
#O(n)

