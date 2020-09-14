#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 -> i-1 :a
        # i -> j-1 :b
        # j -> k   :XX
        # k+1 -> -1:c
        i = j = 0
        length = len(nums)
        k = length-1
        if not nums or length<2:
            return 
        while j<=k:
            curr = nums[j]#current element
            if curr==0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j+=1
            elif curr==1:
                j+=1
            else:
                nums[k],nums[j] = nums[j],nums[k]
                k-=1
                # j stay unchanged since nums[j] is new
        

# @lc code=end
# three pointers
