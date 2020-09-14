#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
# https://leetcode-cn.com/problems/summary-ranges/description/
#
# algorithms
# Medium (53.57%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    13.2K
# Total Submissions: 24.7K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
# 
# 示例 1:
# 
# 输入: [0,1,2,4,5,7]
# 输出: ["0->2","4->5","7"]
# 解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
# 
# 示例 2:
# 
# 输入: [0,2,3,4,6,8,9]
# 输出: ["0","2->4","6","8->9"]
# 解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
# 
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for num in nums:
            if not ranges or num>ranges[-1][-1]+1:
                ranges += [],
            ranges[-1][1:] = num,
        return ['->'.join(map(str, r)) for r in ranges]
# @lc code=end
# [], => [[]]
# num, => [num]