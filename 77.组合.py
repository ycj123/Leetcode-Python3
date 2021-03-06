#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (74.53%)
# Likes:    338
# Dislikes: 0
# Total Accepted:    72.5K
# Total Submissions: 97.2K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n<1:
            return []
        candidate = [i for i in range(1, n+1)]
        res = []
        def helper(candidate, path):
            if len(path) == k:
                res.append(path)
                return
            if not candidate:
                return
            helper(candidate[1:], path+[candidate[0]])
            helper(candidate[1:], path)
        helper(candidate, [])
        return res
# @lc code=end  

