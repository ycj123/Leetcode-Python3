#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
#中心扩散法
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length<2:#special case
            return s

        def helper(left,right):
            while left>=0 and right<length and s[left]==s[right]:#boundary at first
                left-=1
                right+=1
            return s[left+1:right], right-left-1 #palindrome, length 

        max_len = 0
        res = ''
        for i in range(length-1):# begin at every char 
            odd_str, odd_len = helper(i,i)# from same char
            even_str, even_len = helper(i, i+1)# from Adjacent chars
            if odd_len>max_len:
                res = odd_str
                max_len = odd_len
            if even_len>max_len:
                res = even_str
                max_len = even_len
        return res
# @lc code=end

