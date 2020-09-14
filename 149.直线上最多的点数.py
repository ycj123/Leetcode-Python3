#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode-cn.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (23.04%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 68.5K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
# 
# 示例 1:
# 
# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
# 
# 示例 2:
# 
# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# 
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import Counter, defaultdict
        points_num = Counter(tuple(point) for point in points)
        not_repeat_points = list(points_num.keys())
        size = len(not_repeat_points)
        if size==1:
            return points_num[not_repeat_points[0]]
        res = 0

        def gcd(x, y):
            if y==0:
                return x
            else:
                return gcd(y, x%y)
        
        for i in range(size-1):
            x1, y1 = not_repeat_points[i]
            slope = defaultdict(int)
            for j in range(i+1, size):
                x2, y2 = not_repeat_points[j]
                dx, dy = x2-x1, y2-y1
                g = gcd(dx, dy)
                if g!=0:
                    dx //= g
                    dy //= g
                currSlope = '{}/{}'.format(dy, dx)
                slope[currSlope] += points_num[(x2, y2)]
            currSlopePoints = points_num[(x1, y1)] + max(slope.values())
            res = max(res, currSlopePoints)
        return res
# @lc code=end
# 实现题
# 对每一对点求斜率 统计同斜率点的个数
