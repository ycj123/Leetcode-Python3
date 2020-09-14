#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (38.64%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    20.9K
# Total Submissions: 54.1K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 
# 说明：
# 
# 
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# 示例 2：
# 
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        import functools
        if not wordDict:
            return []
        wordDict = set(wordDict)
        max_len = max(map(len, wordDict))

        @functools.lru_cache(None)
        def helper(s):
            res = []
            if not s:
                res.append('')
                return res
            for i in range(len(s)):#end of left half
                if i<max_len and s[:i+1] in wordDict:#match
                    for t in helper(s[i+1:]):
                        if not t:
                            res.append(s[:i+1])
                        else:
                            res.append(s[:i+1] + ' ' + t)
            return res
        return helper(s)
# @lc code=end

