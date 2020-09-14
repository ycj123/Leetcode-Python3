#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (42.23%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    70.6K
# Total Submissions: 167.1K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        helper = {}
        def find(x):
            helper.setdefault(x, x)
            if helper[x]!=x:
                helper[x] = find(helper[x])
            return helper[x]
        def union(x, y):
            helper[find(x)] = find(y)
        
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                curr = board[i][j]
                if curr == 'O':
                    if i==0 or j==0 or i==m-1 or j==n-1:
                        union(i*n + j, 'border')
                    else:
                        for x,y in direction:
                            if board[i+x][j+y]=='O':
                                union((i+x)*n+j+y, i*n+j)
        for i in range(m):
            for j in range(n):
                if find(i*n+j)==find('border'):
                    pass
                else:
                    if board[i][j]=='O':
                        board[i][j] = 'X'
        return
# @lc code=end
# 1. bfs
# 2. dfs
# 3. union find
