#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.08%)
# Likes:    1271
# Dislikes: 0
# Total Accepted:    170.5K
# Total Submissions: 224.1K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n<1:
            return res
        def helper(left=0,right=0,path=''):
            if len(path)==2*n and left==n and right==n:
                res.append(path)
                return
            if right > left or left>n or right>n:
                return
            helper(left+1,right,path+'(')
            helper(left,right+1,path+')')
        helper()
        return res
# @lc code=end

