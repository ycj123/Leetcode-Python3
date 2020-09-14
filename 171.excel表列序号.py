#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        helper = {}
        for i in range(26):
            helper[chr(65+i)] = i+1
        for index,i in enumerate(s):
            res += helper[i] * 26 ** (len(s)-1-index)
        return res
# @lc code=end

