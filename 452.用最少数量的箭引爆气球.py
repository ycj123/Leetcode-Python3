#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        length = len(points)
        if length<2:
            return length
        res = 1
        points.sort(key=lambda x: x[1])
        end  = points[0][1]
        for interval in points[1:]:
            if end < interval[0]:
                res += 1
                end = interval[1]
        return res
# @lc code=end

