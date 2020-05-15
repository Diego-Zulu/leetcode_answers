#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (49.89%)
# Likes:    1926
# Dislikes: 406
# Total Accepted:    485.2K
# Total Submissions: 972.4K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Return True if n is a happy number, and False if not.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
#

# @lc code=start
def squares_sum(n):
    su = 0
    while n:
        n, digit = divmod(n, 10)
        su += digit**2
    return su

class Solution:
    def isHappy(self, n: int) -> bool:
        squares = set([0, 1])
        while n not in squares:
            squares.add(n)
            n = squares_sum(n)
        return True if n == 1 else False
# @lc code=end
