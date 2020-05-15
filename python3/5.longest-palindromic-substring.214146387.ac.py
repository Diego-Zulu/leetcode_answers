#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.08%)
# Likes:    6256
# Dislikes: 504
# Total Accepted:    884.5K
# Total Submissions: 3M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        pal = [0, 0]
        for i in range(n-1):
            j = i+1
            dp[j][j] = True
            if s[i] == s[j]:
                pal = [i, j]
                dp[i][j] = True
        for l in range(3, n+1):
            for i in range(0, n-l+1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    pal = [i, j]
                    dp[i][j] = True  
        return s[pal[0]: pal[1]+1]
# @lc code=end
