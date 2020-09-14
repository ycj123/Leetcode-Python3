#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (34.64%)
# Likes:    2136
# Dislikes: 0
# Total Accepted:    446.4K
# Total Submissions: 1.3M
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x<0
        y = abs(x)
        res = 0
        boundry = 1<<31 if isNeg else (1<<31)-1
        while y!=0:
            res = res*10 + y%10
            if res > boundry:
                return 0
            y//=10
        return -res if isNeg else res
# @lc code=end
# (1<<31) - 1  must have bracket
# 
