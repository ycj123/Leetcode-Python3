#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (38.69%)
# Likes:    1234
# Dislikes: 0
# Total Accepted:    345.3K
# Total Submissions: 892.3K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Trie = {}
        for word in strs:
            if not word:
                return ''
            tree = Trie
            for c in word:#build trie
                tree = tree.setdefault(c, {})
            tree['#'] = True#end of string
        prefix = ''
        while Trie:
            if len(Trie)==1:
                c = list(Trie.keys())[0]
                if c=='#':#if this is end of a string
                    break
                prefix += c
                Trie = Trie[c]
            else:
                break
        return prefix

# @lc code=end
# use trie tree

