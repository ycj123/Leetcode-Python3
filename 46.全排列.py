#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def helper(candidate,path):
            if not candidate:
                answer.append(path[:])
                return
            for i in range(len(candidate)):
                helper(candidate[:i]+candidate[i+1:],path+[candidate[i]])
        helper(nums,[])
        return answer
             
# @lc code=end