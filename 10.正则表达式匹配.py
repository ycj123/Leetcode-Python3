#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s#needle is empty
        first_match = bool(s and p[0] in {s[0], '.'})#first one is match or not
        if len(p)>1 and p[1]=='*':#second one in p is *
            return self.isMatch(s, p[2:]) or \
                first_match and self.isMatch(s[1:], p) #ignore first one in p or repeat
        else:
            return first_match and self.isMatch(s[1:], p[1:])
        
                    
# @lc code=end
# aaab
# a*b
# -> 
# aab + a*b or aaab + b
# ab + a*b or aab + b
# b + a*b or ab + b
