#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        direction = [[-1,0], [1,0], [0,-1], [0,1]]
        row = len(grid)
        col = len(grid[0])
        res = 0
        def helper(i, j):
            grid[i][j] = '0'
            for x,y in direction:
                newx = x+i
                newy = y+j
                if row>newx>=0 and col>newy>=0 and grid[newx][newy]=='1':
                    helper(newx, newy) 
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    helper(i,j)
        return res
# @lc code=end
# dfs
