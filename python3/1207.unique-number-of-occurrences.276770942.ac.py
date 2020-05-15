#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
# https://leetcode.com/problems/unique-number-of-occurrences/description/
#
# algorithms
# Easy (71.08%)
# Likes:    300
# Dislikes: 18
# Total Accepted:    45.3K
# Total Submissions: 63.8K
# Testcase Example:  '[1,2,2,1,1,3]'
#
# Given an array of integers arr, write a function that returns true if and
# only if the number of occurrences of each value in the array is unique.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
# values have the same number of occurrences.
# 
# Example 2:
# 
# 
# Input: arr = [1,2]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniq = collections.Counter(arr)
        values = uniq.values()
        return len(set(values)) == len(values)
# @lc code=end
