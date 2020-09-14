#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# 优先匹配长度为2
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        helper = {
            'I':1,
            'V':5,
            'IV':4,
            'X':10,
            'IX':9,
            'L':50,
            'C':100,
            'XL':40,
            'XC':90,
            'D':500,
            'M':1000,
            'CD':400,
            'CM':900
        }
        length = len(s)
        i = 0
        res = 0
        while i < length:
            if s[i:i+2] in helper:
                res += helper[s[i:i+2]]
                i+=2
            else:
                res += helper[s[i]]
                i+=1
        return res
# @lc code=end

