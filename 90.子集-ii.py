#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (60.73%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    47.1K
# Total Submissions: 77.5K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(index, path):
            if path not in res:
                res.append(path)
            for j in range(index, len(nums)):
                helper(j+1, path + [nums[j]])

        res = []
        if not nums:
            return res
        nums.sort()
        helper(0, [])
        return res
# @lc code=end
# sort + if judgement
