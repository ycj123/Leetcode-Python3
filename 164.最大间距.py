#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#
# https://leetcode-cn.com/problems/maximum-gap/description/
#
# algorithms
# Hard (55.06%)
# Likes:    197
# Dislikes: 0
# Total Accepted:    18.4K
# Total Submissions: 33.5K
# Testcase Example:  '[3,6,9,1]'
#
# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
# 
# 如果数组元素个数小于 2，则返回 0。
# 
# 示例 1:
# 
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
# 
# 示例 2:
# 
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
# 
# 说明:
# 
# 
# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
# 
# 
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        gap = math.ceil((max_num - min_num)/(size-1))
        bucket = [[float('inf'), float('-inf')] for _ in range(size-1)]
        # find min and max for each bucket
        for num in nums:
            if num == min_num or num==max_num:
                continue
            index = (num - min_num)//gap
            bucket[index][0] = min(num, bucket[index][0])
            bucket[index][1] = max(num, bucket[index][1])
        # begin from min number
        pre = min_num
        res = 0
        for currmin,currmax in bucket:
            if currmin==float('inf'):
                continue
            res = max(res, currmin-pre)#gap between buckets
            pre = currmax
        res = max(res, max_num-pre)
        return res
# @lc code=end
# bucket sort
# 相邻的最大差值一定不小于该数组的最大值减去最小值除以间隔个数
# 把相邻间隔小于 gap放在一个桶里，那么最大间隔一定在相互桶之间产生！
