#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (24.05%)
# Likes:    2368
# Dislikes: 2594
# Total Accepted:    372.5K
# Total Submissions: 1.5M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#

# @lc code=start
def can_decode(i, decoded):
    if len(decoded) < i + 2:
        return False
    return decoded[i:i+2] <= "26"

class Solution:
    def numDecodings(self, decoded: str) -> int:
        _this = 1
        _next = 0
        for i in range(len(decoded)):
            curr = _this
            _this = _next
            _next = 0
            if decoded[i] == '0':
                continue
            if can_decode(i, decoded):
                _next = curr
            _this += curr
        return _this

# @lc code=end
