#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (68.97%)
# Likes:    358
# Dislikes: 0
# Total Accepted:    44.8K
# Total Submissions: 64.9K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回 s 所有可能的分割方案。
# 
# 示例:
# 
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(s, path):
            if not s:
                res.append(path)
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], path+[s[:i]])
        res = []
        helper(s, [])
        return res
            
# @lc code=end

