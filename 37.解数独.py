#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        canrow = [set(range(1,10)) for _ in range(9)]
        cancol = [set(range(1,10)) for _ in range(9)]
        canblo = [set(range(1,10)) for _ in range(9)]#candidates
        empty_list = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':#hole
                    empty_list.append((i,j))
                else:
                    number = int(board[i][j])#exist numbers
                    canrow[i].remove(number)
                    cancol[j].remove(number)
                    canblo[(i//3)*3+j//3].remove(number)

        def helper(holes):#backtrack helper
            if not holes:#no more candidates
                return True
            i,j = holes.pop(0)
            k = (i//3)*3 + j//3
            for candidate in canrow[i]&cancol[j]&canblo[k]:#possible ones
                board[i][j] = str(candidate)
                canrow[i].remove(candidate)
                cancol[j].remove(candidate)
                canblo[k].remove(candidate)
                if helper(holes[:]):#go deeper
                    return True
                board[i][j] = '.'#back
                canrow[i].add(candidate)
                cancol[j].add(candidate)
                canblo[k].add(candidate)
            return False

        helper(empty_list)
# @lc code=end
#backtrack + set
#python list parameter -> pointer
