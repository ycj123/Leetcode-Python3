#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            pre = res[-1]
            curr = intervals[i]
            if pre[1] < curr[0]:#no intersection
                res.append(curr)
            else:
                res.pop()
                res.append([pre[0], max(curr[1], pre[1])])
        return res
# @lc code=end
# merge with [-1]
