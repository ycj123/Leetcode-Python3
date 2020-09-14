#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#

# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False

        def helper(nums):
            if len(nums)==1:
                if abs(nums[0] - 24) < 1e-6:
                    return True
                else:
                    return False
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i==j:
                        continue
                    rest = [nums[k] for k in range(len(nums)) if i!=k!=j]
                    if helper(rest + [nums[i] + nums[j]]): return True
                    if helper(rest + [nums[i] - nums[j]]): return True
                    if helper(rest + [nums[i] * nums[j]]): return True
                    if nums[j]!=0 and helper(rest + [nums[i] / nums[j]]):
                        return True
            return False
        return helper(nums)
# @lc code=end

