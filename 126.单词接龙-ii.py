#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# https://leetcode-cn.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (38.51%)
# Likes:    318
# Dislikes: 0
# Total Accepted:    23.1K
# Total Submissions: 60.2K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord
# 的最短转换序列。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换后得到的单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: []
# 
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
# 
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordlength = len(beginWord)
        from collections import defaultdict
        helper = defaultdict(list)

        for word in wordList:#store all the neighbours
            for i in range(wordlength):
                curr = word[:i] + '$' + word[i+1:]
                helper[curr].append(word)

        queue = [(beginWord, [beginWord])]
        visited = set()
        visited.add(beginWord)
        res = []
        while queue:
            size = len(queue)
            for _ in range(size):
                current, path = queue.pop(0)
                if current == endWord:
                    res.append(path)
                visited.add(current)
                for i in range(wordlength):
                    templet = current[:i] + '$' + current[i+1:]
                    for neighbour in helper[templet]:
                        if neighbour not in visited:
                            queue.append((neighbour, path + [neighbour]))
        if not res:
            return []
        min_ = min(map(len, res))
        return [i for i in res if len(i)==min_]
# @lc code=end

