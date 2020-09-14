#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        for index,i in enumerate(nums):
            if max_i>=index:
                if index+i>max_i:
                    max_i = index+i
            else:
                return False
        return True
            
# @lc code=end

