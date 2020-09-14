#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        t = n
        while t:
            t-=1
            a,b = divmod(t, 26)
            res = chr(b+65) + res
            t = a
        return res
# @lc code=end

