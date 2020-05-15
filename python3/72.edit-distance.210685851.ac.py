#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (42.28%)
# Likes:    3340
# Dislikes: 51
# Total Accepted:    242.8K
# Total Submissions: 573.8K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following 3 operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n*m == 0:
            return n + m
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i] = i
        for i in range(n+1):
            dp[i][0] = i
        for r in range(1, n+1):
            for c in range(1, m+1):
                last_edit = dp[r-1][c-1]
                if word1[r-1] == word2[c-1]:
                    last_edit -= 1
                dp[r][c] = 1 + min(dp[r][c-1], dp[r-1][c], last_edit)
        return dp[n][m]
# @lc code=end
