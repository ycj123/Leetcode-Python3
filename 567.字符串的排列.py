#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        c1 = Counter(s1)
        start = 0
        end = len(s1)-1
        while end < len(s2):
            if c1 == Counter(s2[start:end+1]):
                return True
            start += 1
            end += 1
        return False
        
# @lc code=end

