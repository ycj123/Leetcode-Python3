#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (38.84%)
# Likes:    727
# Dislikes: 0
# Total Accepted:    75.6K
# Total Submissions: 194.3K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。
# 
# 
# 
# 示例：
# 
# 输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC"
# 
# 
# 
# 提示：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t = Counter(t)
        lookup = Counter()
        start = 0
        end = 0
        min_l = float('inf')
        res = ''
        while end < len(s):#slide right end to include new char
            lookup[s[end]] += 1
            end +=1
            while all(map(lambda x:lookup[x]>=t[x], t.keys())):#still satisify
                if end - start < min_l:#update result
                    min_l = end - start
                    res = s[start:end]
                lookup[s[start]]-=1#slide left end 
                start += 1
        return res
# @lc code=end
# slide window
# counter rather than dictionary
