#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (62.51%)
# Likes:    344
# Dislikes: 0
# Total Accepted:    78.7K
# Total Submissions: 125.8K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        candidates.sort()#sort to prevent duplicate
        
        def helper(candi, path):
            if sum(path) == target:#find result
                res.append(path)
                return
            elif sum(path) > target:
                return 
            for i in range(len(candi)):
                if i>0 and candi[i]==candi[i-1]:
                    continue
                helper(candi[i+1:], path+[candi[i]])#move forward
        helper(candidates, [])
        return res
            
# @lc code=end
# backtrack
# prevant duplicate:
# 1. sort 2. i>0 and [i]==[i-1]