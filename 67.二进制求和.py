#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (54.43%)
# Likes:    462
# Dislikes: 0
# Total Accepted:    122.8K
# Total Submissions: 225.8K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 
# 输入为 非空 字符串且只包含数字 1 和 0。
# 
# 
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 
# 
# 提示：
# 
# 
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(i) for i in a]
        b = [int(i) for i in b]
        carry = 0
        res = ''
        while a or b:
            if not a:
                a.append(0)
            if not b:
                b.append(0)
            carry += a.pop() + b.pop()
            res = str(carry%2) + res
            carry//=2
        if carry:
            return '1'+res
        return res

# @lc code=end

