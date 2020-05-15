#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (33.33%)
# Likes:    1201
# Dislikes: 1802
# Total Accepted:    523.2K
# Total Submissions: 1.6M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]: return x
        start = 1
        end = x - 1
        while start < end - 1:
            mid = int((start + end)/2)
            if mid*mid > x:
                end = mid
            else:
                start = mid
        return end if end*end <= x else start

# @lc code=end
