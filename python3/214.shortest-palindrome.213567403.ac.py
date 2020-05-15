#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (29.30%)
# Likes:    1030
# Dislikes: 111
# Total Accepted:    93.9K
# Total Submissions: 320.1K
# Testcase Example:  '"aacecaaa"'
#
# Given a string s, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.
# 
# Example 1:
# 
# 
# Input: "aacecaaa"
# Output: "aaacecaaa"
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: "dcbabcd"
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        pattern = s + '#' + rev
        n = len(pattern)
        kmp = [0] * n
        for i in range(1, n):
            j = kmp[i-1]
            while j > 0 and pattern[i] != pattern[j]:
                j = kmp[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            kmp[i] = j
        return rev[:len(s) - kmp[n - 1]] + s
# @lc code=end
