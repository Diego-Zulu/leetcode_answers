#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (41.55%)
# Likes:    2523
# Dislikes: 165
# Total Accepted:    205.7K
# Total Submissions: 494.4K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        letter_count = collections.Counter(p)
        letters = len(p)
        left, N, starts = 0, len(s), []
        for i, c in enumerate(s):
            while left < i and c in letter_count and letter_count[c] == 0:
                letter_count[s[left]] += 1
                left += 1
                letters += 1
            if c in letter_count:
                letter_count[c] -= 1
                letters -= 1
                if letters == 0:
                    starts.append(left)
                    letter_count[s[left]] += 1
                    left += 1
                    letters += 1
            else:
                left = i + 1
                letter_count = collections.Counter(p)
                letters = len(p)
        return starts
                
            
# @lc code=end
