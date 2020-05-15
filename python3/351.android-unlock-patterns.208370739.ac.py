#
# @lc app=leetcode id=351 lang=python3
#
# [351] Android Unlock Patterns
#
# https://leetcode.com/problems/android-unlock-patterns/description/
#
# algorithms
# Medium (47.79%)
# Likes:    353
# Dislikes: 526
# Total Accepted:    39.5K
# Total Submissions: 82.6K
# Testcase Example:  '1\n1'
#
# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤
# n ≤ 9, count the total number of unlock patterns of the Android lock screen,
# which consist of minimum of m keys and maximum n keys.
# 
# 
# 
# Rules for a valid pattern:
# 
# 
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any
# other keys, the other keys must have previously selected in the pattern. No
# jumps through non selected key is allowed.
# The order of keys used matters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Explanation:
# 
# 
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# 
# Invalid move: 4 - 1 - 3 - 6 
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.
# 
# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.
# 
# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected
# in the pattern
# 
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected
# in the pattern.
# 
# 
# 
# Example:
# 
# 
# 
# Input: m = 1, n = 1
# Output: 9
# 
# 
# 
#

# @lc code=start
ONE_STEP = {
    1: [2,4,5,8,6],
    2: [1,4,5,6,3,7,9], 
    3: [2,5,6,8,4],
    4: [1,2,5,8,7,3,9],
    5: [1,2,3,4,6,7,8,9],
    6: [2,3,5,8,9,7,1],
    7: [4,5,8,2,6],
    8: [7,4,5,6,9,1,3],
    9: [8,5,6,4,2],
}

TWO_STEP = {
    1: [(2,3), (5,9), (4,7)],
    2: [(5,8)],
    3: [(2,1),(5,7),(6,9)],
    4: [(5,6)],
    5: [],
    6: [(5, 4)],
    7: [(4, 1), (5,3), (8, 9)],
    8: [(5, 2)],
    9: [(8, 7), (5, 1), (6, 3)],
}

def numberOfPatternsAux(m, n, visited, next_numb):
    if n == 0:
        return 1
    paths_sum = 0 if m > 0 else 1
    new_m = max(0, m-1)
    new_n = max(0, n-1)
    for i in ONE_STEP[next_numb]:
        if i not in visited:
            visited.add(i)
            paths_sum += numberOfPatternsAux(new_m, new_n, visited, i)
            visited.remove(i)
    for middle, i in TWO_STEP[next_numb]:
        if i not in visited and middle in visited:
            visited.add(i)
            paths_sum += numberOfPatternsAux(new_m, new_n, visited, i)
            visited.remove(i)
    return paths_sum

class Solution:
    def numberOfPatterns(self, m: 'int', n: 'int') -> 'int':
        paths_sum = 0
        for i in range(1, 10):
            paths_sum += numberOfPatternsAux(m-1, n-1, set([i]), i)
        return paths_sum
        
        
# @lc code=end
