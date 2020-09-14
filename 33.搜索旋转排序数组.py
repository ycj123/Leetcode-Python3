#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        length = len(nums)
        right = length-1
        if not nums:
            return -1
        while left < right:
            mid = left + (right-left)//2
            a = nums[left]
            b = nums[mid]
            c = nums[right]
            if a<=b:# = because using left median
                if a<=target<=b:
                    right = mid
                else:
                    left = mid+1
            else:
                if b<=target<=c:
                    left = mid
                else:
                    right = mid-1
        return left if nums[left]==target else -1
        
# @lc code=end

