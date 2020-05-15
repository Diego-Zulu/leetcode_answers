#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#
# https://leetcode.com/problems/repeated-string-match/description/
#
# algorithms
# Easy (32.15%)
# Likes:    726
# Dislikes: 696
# Total Accepted:    88.2K
# Total Submissions: 274.3K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# Given two strings A and B, find the minimum number of times A has to be
# repeated such that B is a substring of it. If no such solution, return -1.
# 
# For example, with A = "abcd" and B = "cdabcdab".
# 
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a
# substring of it; and B is not a substring of A repeated two times
# ("abcdabcd").
# 
# Note:
# The length of A and B will be between 1 and 10000.
# 
#

# @lc code=start
import math

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        repeated_A = A
        repeated_times = 1
        
        while len(repeated_A) < len(B):
            repeated_A += A
            repeated_times += 1
            
        if B in repeated_A:
            return repeated_times
        elif B in (repeated_A + A):
            return repeated_times + 1
        else:
            return -1
        
        
# @lc code=end
