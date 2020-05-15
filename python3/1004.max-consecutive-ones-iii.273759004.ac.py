#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (57.49%)
# Likes:    830
# Dislikes: 20
# Total Accepted:    44.3K
# Total Submissions: 77K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# 
# Return the length of the longest (contiguous) subarray that contains only
# 1s. 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# Example 2:
# 
# 
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1 
# 
# 
# 
#

# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = longest = 0
        current_k = K
        for right in range(len(A)):
            if A[right] == 0:
                current_k -= 1
                while current_k < 0:
                    current_k += 1 if A[left] == 0 else 0
                    left += 1
            longest = max(longest, right - left + 1)
        return longest
# @lc code=end
