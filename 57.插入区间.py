#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (37.59%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    28.8K
# Total Submissions: 76.5K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 
# 
# 
# 示例 1：
# 
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 
# 
# 示例 2：
# 
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 
# 
# 
# 
# 注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。
# 
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        i = 0
        res = []

        while i<len(intervals) and left > intervals[i][1]:#before middle
            res.append(intervals[i])
            i+=1

        middle = [left, right] #maybe end of intervals
        while i<len(intervals) and right >= intervals[i][0]:#find end of middle
            middle[0] = min(middle[0], intervals[i][0])
            middle[1] = max(middle[1], intervals[i][1])
            i+=1
        res.append(middle)

        while i<len(intervals):
            res.append(intervals[i])
            i+=1
        return res

# @lc code=end
# 1. before middle , just append
# 2. find right middle then append
# 3. after middle , just append
