#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import defaultdict
        from copy import deepcopy
        helper = defaultdict(int)
        if not s or not words:
            return []
        res = []
        wc = len(words)
        wl = len(words[0])
        for word in words:
            helper[word] += 1
        for i in range(len(s) - wc*wl+1):
            curr = s[i:i+wl*wc]
            t = deepcopy(helper)#copy hash table
            for j in range(i, len(curr)+i, wl):
                p = s[j:j+wl]
                if p in t:#match
                    t[p] -= 1
                    if t[p] == 0:
                        t.pop(p)
                else:#not match
                    break
                if not t:#empty table
                    res.append(i)
        return res


# @lc code=end
# hash table store all the candidates 
# deepcopy
