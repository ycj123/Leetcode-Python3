#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#
# https://leetcode-cn.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (36.30%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    23.3K
# Total Submissions: 64.2K
# Testcase Example:  '"aacecaaa"'
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
# 
# 示例 1:
# 
# 输入: "aacecaaa"
# 输出: "aaacecaaa"
# 
# 
# 示例 2:
# 
# 输入: "abcd"
# 输出: "dcbabcd"
# 
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
# @lc code=end

