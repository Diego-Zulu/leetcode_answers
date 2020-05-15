#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (41.49%)
# Likes:    794
# Dislikes: 166
# Total Accepted:    209.5K
# Total Submissions: 505.2K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Follow up: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return False
        l = 1
        r = num // 2 + 1
        while l < r:
            m = l + (r-l)//2
            mult = m*m
            if mult == num:
                return True
            elif mult > num:
                r = m
            else:
                l = m + 1
        return l*l == num
# @lc code=end
