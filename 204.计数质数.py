#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        helper = [1]*n
        helper[0] = helper[1] = 0
        for i in range(2,n//2+1):
            if helper[i] == 1:
                for j in range(i*2,n,i):
                    helper[j] = 0
        return sum(helper)
# @lc code=end

