#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2 = len(nums1), len(nums2)
        if l1>l2:
            return self.findMedianSortedArrays(nums2,nums1) #search short one for efficiency
        isOdd = (l1+l2) & 0x1 # whole list length is odd or even
        k = (l1+l2+1) // 2 # find the kth element
        
        l, r = 0, l1 #result can be 0 -> l1 
        while l < r:# search in nums1
            mid = (l+r)//2
            if nums1[mid]<nums2[k-mid-1]:# exclusive if : b < c is not acceptable
                l = mid+1
            else:
                r = mid
        m1 = l
        m2 = k-m1 # find c1
        if m1==0:# all in nums2
            c1 = nums2[m2-1]
        elif m2==0:# all in nums1
            c1 = nums1[m1-1]
        else:
            c1 = max(nums1[m1-1],nums2[m2-1])

        if isOdd:# find c2
            return c1
        else:# is even
            if m1==l1:# c2 in nums2
                c2 = nums2[m2]
            elif m2==l2:# c2 in nums1
                c2 = nums1[m1]
            else:
                c2 = min(nums1[m1],nums2[m2])
            return (c1+c2)/2
# @lc code=end
# find kth element
# find the right position in s1 and right position in s2 at the same time
# how to find the position in s1
#  ... a/b ...
 # ... c/d ...
 # a<d and c<d => find the answer
 # if length is odd: max(a,c)
 # if length is even: (max(a,c), min(b,d))//2
 # sorted list + search => binary search

