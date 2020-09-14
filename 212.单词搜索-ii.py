#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        direction = [[1,0], [-1,0], [0,-1], [0,1]]
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = True
            
        def search(i, j, node, pre, visited):
            if '#' in node:
                res.add(pre)
            for x,y in direction:
                newx, newy = x+i, y+j
                # c = board[newx][newy]
                if -1<newx<row and -1<newy<col and board[newx][newy] in node and (newx,newy) not in visited:
                    search(newx, newy, node[board[newx][newy]], pre+board[newx][newy], visited | {(newx,newy)})
        res = set()
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                c = board[i][j]
                if c in trie:
                    search(i, j, trie[c], c, {(i,j)})
        return list(res)
# @lc code=end

