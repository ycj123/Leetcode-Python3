#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        if n<2:
            return 0
        d = 2
        res = 0
        dummy = n
        while n>1:
            while n%d==0:
                res += d
                n//=d
            d+=1
            if d>(dummy/2):
                if res==0:
                    res+=dummy
                break
        return res
# @lc code=end

