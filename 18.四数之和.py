#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (38.34%)
# Likes:    552
# Dislikes: 0
# Total Accepted:    102.6K
# Total Submissions: 267.4K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        res = []
        nums.sort()
        for i in range(length):
            if i>0 and nums[i]==nums[i-1]:#remove duplicate
                continue
            for j in range(i+1,length):
                if j>i+1 and nums[j]==nums[j-1]:###remove duplicate
                    continue
                left = j+1
                right = length-1
                while left < right:
                    currsum = nums[i]+nums[j]+nums[left]+nums[right]
                    if currsum==target:
                        res.append([nums[i],nums[j], nums[left], nums[right]])
                        while left < right and nums[left]==nums[left+1]:
                            left += 1
                        while left < right and nums[right]==nums[right-1]:
                            right-=1
                        left += 1
                        right -=1
                    elif currsum<target:
                        left += 1
                    else:
                        right -=1
        return res
# @lc code=end
# sort + double pointer
# remove duplicate
