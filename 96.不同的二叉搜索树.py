#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (69.08%)
# Likes:    787
# Dislikes: 0
# Total Accepted:    83.5K
# Total Submissions: 120.9K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):# current n
            for j in range(i):#0 -> n-1
                dp[i] += dp[j] * dp[i-1-j]
        return dp[-1]
# @lc code=end      
# G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)

# n为根节点，当i为根节点时，其左子树节点个数为[1,2,3,...,i-1]，

# 右子树节点个数为[i+1,i+2,...n]，
# 所以当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，
# 即 f(i) = G(i-1)*G(n-i)

# 上面两式可得:G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)

