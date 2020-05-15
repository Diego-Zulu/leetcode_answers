#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (33.95%)
# Likes:    3998
# Dislikes: 282
# Total Accepted:    370.3K
# Total Submissions: 1.1M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#

# @lc code=start
MIN_CHAR = ord(' ')
MAX_CHAR = ord('~')
RANGE = MAX_CHAR - MIN_CHAR + 1

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        present_c = [0 for i in range(RANGE)]
        m = len(t)
        n = len(s)
        minWindow = [-1, n]
        for c in t:
            present_c[ord(c) - MIN_CHAR] += 1
        low = 0
        for high in range(n):
            ascii_pos = ord(s[high]) - MIN_CHAR
            present_c[ascii_pos] -= 1
            if present_c[ascii_pos] >= 0:
                m -= 1
                while m == 0:
                    minWindow = min(minWindow, [low, high], key= lambda x: x[1] - x[0])
                    ascii_pos = ord(s[low]) - MIN_CHAR
                    present_c[ascii_pos] += 1
                    if present_c[ascii_pos] > 0:
                        m += 1
                    low += 1
        if minWindow[0] == -1:
            return ""
        return s[minWindow[0]:minWindow[1]+1]
# @lc code=end
