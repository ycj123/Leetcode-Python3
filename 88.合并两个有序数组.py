#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        p = m+n-1
        while p1>=0 and p2>=0:
            n1 = nums1[p1]
            n2 = nums2[p2]
            if n1>n2:
                nums1[p],nums1[p1] = nums1[p1],nums1[p]
                p1-=1
            else:
                nums1[p],nums2[p2] = nums2[p2],nums1[p]
                p2-=1
            p-=1
        nums1[:p2+1] = nums2[:p2+1]
        
# @lc code=end

