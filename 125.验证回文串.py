#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:     
        s = re.sub('[\W_]','', s) # _
        if not s:
            return True
        length = len(s)
        mid = length // 2
        for i in range(mid):
            if s[i].lower() != s[-1-i].lower():
                return False
        return True

# @lc code=end

