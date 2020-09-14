#
# @lc app=leetcode.cn id=672 lang=python3
#
# [672] 灯泡开关 Ⅱ
#

# @lc code=start
class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if n==0 or m==0:
            return 1
        if n==1:
            return 2
        elif n==2 and m==1:
            return 3
        elif n==2 or m==1:
            return 4
        if m==2:
            return 7
        return 8
# @lc code=end

