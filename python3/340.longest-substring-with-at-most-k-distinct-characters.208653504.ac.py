#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Hard (43.34%)
# Likes:    985
# Dislikes: 35
# Total Accepted:    123.6K
# Total Submissions: 285K
# Testcase Example:  '"eceba"\n2'
#
# Given a string, find the length of the longest substring T that contains at
# most k distinct characters.
# 
# Example 1:
# 
# 
# 
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.
# 
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: 'str', k: 'int') -> 'int':
        distinct = defaultdict(lambda: 0)
        distinct_numb = 0
        l = 0
        max_l = 0
        for r in range(len(s)):
            c_code = ord(s[r])
            distinct[c_code] += 1
            if distinct[c_code] == 1:
                distinct_numb += 1
            if distinct_numb <= k:
                max_l = max(max_l, r - l + 1)
            while distinct_numb > k:
                c_code = ord(s[l])
                distinct[c_code] -= 1
                if distinct[c_code] == 0:
                    distinct_numb -= 1
                l+=1
        return max_l
# @lc code=end
