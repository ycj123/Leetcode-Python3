#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (37.23%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    23.8K
# Total Submissions: 63.7K
# Testcase Example:  '"3+2*2"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
# 
# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
# 
# 示例 1:
# 
# 输入: "3+2*2"
# 输出: 7
# 
# 
# 示例 2:
# 
# 输入: " 3/2 "
# 输出: 1
# 
# 示例 3:
# 
# 输入: " 3+5 / 2 "
# 输出: 5
# 
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
        num = 0
        sign = '+'
        s += '+0'
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char in {'+', '-', '*', '/'}:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                else:
                    if stack[-1]<0:
                        stack[-1] = -(-stack[-1] // num)
                    else:
                        stack[-1] = stack[-1] // num
                sign, num = char, 0
        return sum(stack)

# @lc code=end
# 负数取整
