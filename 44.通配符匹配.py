#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
# https://leetcode-cn.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (31.25%)
# Likes:    505
# Dislikes: 0
# Total Accepted:    51.5K
# Total Submissions: 164.8K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# 
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 
# 
# 两个字符串完全匹配才算匹配成功。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 
# 
# 示例 3:
# 
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 
# 
# 示例 4:
# 
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 
# 
# 示例 5:
# 
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = len(p) + 1
        j = len(s) + 1
        table = [[False]*j for _ in range(i)]
        table[0][0] = True

        if p.startswith('*'):# use startswith : maybe empty
            table[1] = [True]*j
        for index in range(len(p)):#multi * : still can be empty
            if p[index]=='*':
                table[index+1][0]=True
            else:
                break

        for m in range(1, i):#p
            for n in range(1, j):#s
                if p[m-1]==s[n-1] or p[m-1]=='?':
                    table[m][n] = table[m-1][n-1]
                if p[m-1]=='*' and table[m-1][n]:
                    table[m][n:] = [True]*(len(s[n:])+1)
        return table[-1][-1]
# @lc code=end
# use table
# * : [i-1][j]
# ? match : [i-1][j-1]
