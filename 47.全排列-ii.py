#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()# sort to aviod duplicate
        def helper(candidate,path):
            if not candidate:
                answer.append(path)
                return
            for i in range(len(candidate)):
                if i>0 and candidate[i]==candidate[i-1]:# remove duplicate
                    continue
                helper(candidate[:i]+candidate[i+1:],path+[candidate[i]])# move i
        helper(nums,[])
        return answer
# @lc code=end

