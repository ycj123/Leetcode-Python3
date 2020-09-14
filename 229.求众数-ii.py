#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
# https://leetcode-cn.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (43.52%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    20.5K
# Total Submissions: 47.1K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
# 
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: [3]
# 
# 示例 2:
# 
# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2 = 0, 0
        candi1, candi2 = 0, 1#different
        for num in nums:
            if num==candi1:
                count1 += 1
            elif num==candi2:
                count2 += 1
            elif count1 == 0:
                candi1 = num
                count1 = 1
            elif count2 == 0:
                candi2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in [candi1, candi2] if nums.count(n)>len(nums)//3]
# @lc code=end
# 最多有两个结果
# 投票法找到top 2

