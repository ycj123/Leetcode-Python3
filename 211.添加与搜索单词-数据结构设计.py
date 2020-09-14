#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (46.13%)
# Likes:    157
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 33.1K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 如果数据结构中有任何与word匹配的字符串，则bool search（word）返回true，否则返回false。 单词可能包含点“。”
# 点可以与任何字母匹配的地方。
# 
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
# 
# 实现词典类 WordDictionary ：
# 
# 
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些
# '.' ，每个 . 都可以表示任何一个字母。
# 
# 
# 
# 
# 示例：
# 
# 输入：
# 
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
# 
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= word.length <= 500
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最调用多 50000 次 addWord 和 search
# 
# 
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.lookup
        for char in word:
            tree = tree.setdefault(char, {})
        tree['$'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(word, tree):
            if not word:
                if '$' in tree:
                    return True
                else:
                    return False
            if word[0] == '.':
                for node in tree:
                    if helper(word[1:], tree[node]):
                        return True
            elif word[0] in tree:
                if helper(word[1:], tree[word[0]]):
                    return True
            return False
        return helper(word, self.lookup)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
# trie
