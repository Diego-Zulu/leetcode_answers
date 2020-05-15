#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (39.09%)
# Likes:    955
# Dislikes: 120
# Total Accepted:    148.4K
# Total Submissions: 379.6K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
# 
# Example 1:
# 
# 
# Input: [5,7]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: [0,1]
# Output: 0
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = n - m
        mult = 1
        sub = 2147483647
        while mult <= diff:
            sub = sub << 1
            mult = mult << 1
        return m & n & sub
# @lc code=end
