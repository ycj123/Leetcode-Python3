#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (38.64%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    19.6K
# Total Submissions: 50.7K
# Testcase Example:  '"1 + 1"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
# 
# 字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
# 
# 示例 1:
# 
# 输入: "1 + 1"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: " 2-1 + 2 "
# 输出: 3
# 
# 示例 3:
# 
# 输入: "(1+(4+5+2)-3)+(6+8)"
# 输出: 23
# 
# 说明：
# 
# 
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        num = 0
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '+':
                res += sign * num
                num = 0
                sign = 1
            elif char == '-':
                res += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                res += sign*num
                num = 0
                res = stack.pop() * res + stack.pop()
        res += sign*num
        return res
# @lc code=end
# use stack
