#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (47.60%)
# Likes:    654
# Dislikes: 0
# Total Accepted:    88.7K
# Total Submissions: 186.3K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top down
        import functools
        wordDict = set(wordDict)
        if not wordDict:
            return not s
        max_len = max(map(len, wordDict))
        @functools.lru_cache(None)
        def helper(s):
            if not s:
                return True
            for i in range(len(s)):
                if i<max_len and s[:i+1] in wordDict and helper(s[i+1:]):
                    return True
            return False

        return helper(s)
# @lc code=end
# bottom up
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         if not wordDict: 
#             return not s
#         dp = [False] * (n + 1)
#         dp[0] = True
#         for i in range(1, n + 1):
#             for j in range(i - 1, -1, -1):
#                 if dp[j] and s[j:i] in wordDict:
#                     dp[i] = True
#                     break
#         return dp[-1]