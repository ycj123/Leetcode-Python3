#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        for i in s:
            if i == '(':
                left += 1
            else:
                right += 1
            if right > left:
                left = 0
                right = 0
            elif right == left:
                res = max(res, left+right)
        left = right = 0
        for i in s[::-1]:
            if i == '(':
                left += 1
            else:
                right += 1
            if left > right:
                left = 0
                right = 0
            elif right == left:
                res = max(res, left + right)
        return res
# @lc code=end
# from left -> right : begin from left
# from right -> left : begin from right
