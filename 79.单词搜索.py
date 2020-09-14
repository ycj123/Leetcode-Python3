#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        note = set()
        if not board:
            return False
        direcation = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows = len(board)
        cols = len(board[0])

        def helper(x, y, index_w):
            if index_w == len(word) - 1:
                return word[-1] == board[x][y]
            if board[x][y] == word[index_w]:
                note.add((x, y))
                index_w += 1
                for d in direcation:
                    newx = x + d[0]
                    newy = y + d[1]
                    if newx < 0 or newx >= rows or newy < 0 or newy >= cols or ((newx,newy) in note):
                        continue
                    if helper(newx, newy, index_w):
                        return True
                note.remove((x, y))
                return False

        for i in range(rows):
            for j in range(cols):
                if helper(i, j, 0): return True
        return False   
        
# @lc code=end

