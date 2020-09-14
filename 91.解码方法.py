#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(1,len(s)):#index of char
            curr = s[i]
            pre = s[i-1]
            if curr == '0':
                if pre == '1' or pre == '2':#10 20 are only possibles
                    dp[i+1] = dp[i-1]#dp[i] is not appropriate
                else:
                    return 0
            else:#not 0
                if 10<int(pre+curr)<27:#26 2 6
                    dp[i+1] = dp[i-1] + dp[i]
                else:
                    dp[i+1] = dp[i]
        return dp[-1]
# @lc code=end

