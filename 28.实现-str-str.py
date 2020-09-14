#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or len(needle) == 0 :
            return 0
        n = len(needle)
        i = 0
        while i <= (len(haystack)-n):   ##等于两个字符串长度相减时，移位完毕
            if haystack[i:i+n] == needle:  ##依次移位，判断i+n（n为第二个字符串长度）是否相等
                return i
            else:
                i += 1
        if i > (len(haystack)-n):
            return -1
# @lc code=end

