#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        m = prices[0]
        res = 0
        for i in prices[1:]:
            if i > m:# higher price
                res = max(res, i-m)
            else:# lower price
                m = i
        return res
# @lc code=end

