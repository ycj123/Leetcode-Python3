#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot = nums[left]
            j = left
            for i in range(left+1,right+1):
                if nums[i]<pivot:
                    j+=1
                    nums[i],nums[j] = nums[j], nums[i]
            nums[left], nums[j] = nums[j], nums[left]
            return j
        
        size = len(nums)
        left = 0
        right = size-1
        while True:
            index = partition(left, right)
            if index == size-k:
                return nums[index]
            elif index < size-k:
                left = index+1
            else:
                right = index-1
        return nums[left]
# @lc code=end
# partition
