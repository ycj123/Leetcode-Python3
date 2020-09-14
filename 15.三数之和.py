#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        nums.sort()#nlgn
        for i in range(length):#pick a
            a = nums[i]
            if (i>0 and nums[i-1]==a) or a+nums[length-1]+nums[length-2]<0:
                continue# remove repeat elements and skip too small a
            if a>0:# all the rest a is not possible to form answers
                break
            left = i+1#next element
            right = length-1#last element
            while left<right:
                if a+nums[left]+nums[right]==0:#answer
                    res.append([a,nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        left +=1# skip duplicate left
                    while left<right and nums[right]==nums[right-1]:
                        right -=1# skip duplicate right
                    left+=1
                    right-=1
                elif a+nums[left]+nums[right]<0:
                    left+=1
                else:
                    right-=1
        return res
# @lc code=end

