#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (40.69%)
# Likes:    1166
# Dislikes: 52
# Total Accepted:    88K
# Total Submissions: 215.9K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# 
# 
# 
# Note:
# 
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# 
#

# @lc code=start
class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		if len(s1) > len(s2):
			return False        
		hash_s1 = 0
		hash_s2 = 0
		d = len(s1)
		for i in range(d):
			hash_s1 += hash(s1[i])
			hash_s2 += hash(s2[i])
		if hash_s1 == hash_s2:
			return True
		for i in range(d, len(s2)):
			hash_s2 += hash(s2[i]) - hash(s2[i - d])
			if hash_s1 == hash_s2:
				return True
		return False
        
# @lc code=end
