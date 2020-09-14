#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon)
        col = len(dungeon[0])
        helper = [[float('inf')]*(col+1) for _ in range(row+1)]
        helper[row][col-1] = 1
        helper[row-1][col] = 1
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                helper[i][j] = max(1, min(helper[i+1][j], helper[i][j+1]) - dungeon[i][j])
        return helper[0][0]

# @lc code=end
#all the time hp>0
