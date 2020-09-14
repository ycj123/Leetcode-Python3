#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (27.38%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 55.6K
# Testcase Example:  '1\n2'
#
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
# 
# 如果小数部分为循环小数，则将循环的部分括在括号内。
# 
# 示例 1:
# 
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
# 
# 
# 示例 2:
# 
# 输入: numerator = 2, denominator = 1
# 输出: "2"
# 
# 示例 3:
# 
# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"
# 
# 
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return '0'
        res = []
        if numerator*denominator<0:
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        if b==0:
            return ''.join(res)
        res.append('.')
        helper = dict()
        helper[b] = len(res)
        while b:
            b*=10
            a, b = divmod(b, denominator)
            res.append(str(a))
            if b in helper:
                res.insert(helper[b], '(')
                res.append(')')
                break
            helper[b] = len(res)
        return ''.join(res)
# @lc code=end
# numerator == 0
# negative
# int part
# float part
# memory numerator and its position
