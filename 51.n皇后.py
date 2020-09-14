#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (70.81%)
# Likes:    516
# Dislikes: 0
# Total Accepted:    58.4K
# Total Submissions: 82.4K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 示例:
# 
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自
# 百度百科 - 皇后 ）
# 
# 
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sample = '.'*n
        res = []
        def helper(level=0, col=set(), left=set(), right=set(), path=[]):
            if level == n:#enough level
                res.append(path)
            for j in range(n):#place queen in possible position in next level
                if j not in col and level-j not in right and level+j not in left:
                    helper(level+1, col|{j}, left|{level+j}, right|{level-j}, path + [sample[:j]+'Q'+sample[j+1:]])
        helper()
        return res
# @lc code=end
# queen : vertical horiziontal X
# 1.horiziiontal : each time add a new level with only one queen
# 2.vertical: column set to store used column
# 3./ : i + j 
# 4.\ : i - j
