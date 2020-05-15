#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (27.76%)
# Likes:    3121
# Dislikes: 130
# Total Accepted:    268.9K
# Total Submissions: 968.6K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#

# @lc code=start
def left_scan(s):
    l, r = 0, 0
    max_size = 0
    for c in s:
        if c == ')':
            r += 1
        else:
            l += 1
        if l == r:
            max_size = max(max_size, r * 2)
        elif l < r:
            l = r = 0
    return max_size

def right_scan(s):
    l, r = 0, 0
    max_size = 0
    for c in s[::-1]:
        if c == ')':
            r += 1
        else:
            l += 1
        if l == r:
            max_size = max(max_size, r * 2)
        elif l > r:
            l = r = 0
    return max_size

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return max(left_scan(s), right_scan(s))
# @lc code=end
