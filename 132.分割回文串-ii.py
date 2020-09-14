#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (43.88%)
# Likes:    187
# Dislikes: 0
# Total Accepted:    15.4K
# Total Submissions: 35.1K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回符合要求的最少分割次数。
# 
# 示例:
# 
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 
# 
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        @functools.lru_cache(None)
        def helper(s):
            res = float('inf')
            if s == s[::-1]:
                return 0
            for i in range(1, len(s)+1):
                if s[:i]==s[:i][::-1]:
                    res = min(helper(s[i:])+1, res)
            return res
        return helper(s)
        
# @lc code=end
# dp
# class Solution:
#     def minCut(self, s: str) -> int:
#         min_s = list(range(len(s)))
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(i+1):
#                 if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
#                     dp[j][i] = True
#                     # 说明不用分割
#                     if j == 0:
#                         min_s[i] = 0
#                     else:
#                         min_s[i] = min(min_s[i], min_s[j - 1] + 1)
#         return min_s[-1]