#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
#
# algorithms
# Medium (38.77%)
# Likes:    174
# Dislikes: 57
# Total Accepted:    12.5K
# Total Submissions: 32.2K
# Testcase Example:  '3\n7'
#
# Return all non-negative integers of length N such that the absolute
# difference between every two consecutive digits is K.
# 
# Note that every number in the answer must not have leading zeros except for
# the number 0 itself. For example, 01 has one leading zero and is invalid, but
# 0 is valid.
# 
# You may return the answer in any order.
# 
# 
# 
# Example 1:
# 
# 
# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading
# zeroes.
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 9
# 0 <= K <= 9
# 
# 
#

# @lc code=start
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return list(range(10))
        else:
            combinations = collections.deque(range(1, 10))
            for _ in range(1, N):
                numb_comb = len(combinations)
                for _ in range(numb_comb):
                    curr_comb = combinations.popleft()
                    last_digit = curr_comb % 10
                    next_digit_pos = last_digit + K
                    next_digit_neg = last_digit - K
                    if next_digit_pos < 10:
                        combinations.append(curr_comb * 10 + next_digit_pos)
                    if next_digit_neg >= 0 and next_digit_neg != next_digit_pos:
                        combinations.append(curr_comb * 10 + next_digit_neg)
            return list(combinations)
# @lc code=end
