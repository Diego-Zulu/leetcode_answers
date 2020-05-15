#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (50.94%)
# Likes:    425
# Dislikes: 139
# Total Accepted:    47.3K
# Total Submissions: 92.9K
# Testcase Example:  '["23:59","00:00"]'
#
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the
# minimum minutes difference between any two time points in the list. 
# 
# Example 1:
# 
# Input: ["23:59","00:00"]
# Output: 1
# 
# 
# 
# Note:
# 
# The number of time points in the given list is at least 2 and won't exceed
# 20000.
# The input time is legal and ranges from 00:00 to 23:59.
# 
# 
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [0] * 1440
        for time in timePoints:
            hour = int(time[0:2])
            minut = int(time[3:5])
            pos = hour*100 - 40*hour + minut
            print(pos)
            print(type(pos))
            print(len(minutes))
            if minutes[pos] > 0:
                return 0
            minutes[pos] = 1
        first_pos, n = 0, len(minutes)
        for i in range(n):
            if minutes[i] > 0:
                first_pos = i
                break
        min_diff = 2400
        min_pos = first_pos
        for i in range(first_pos+1, n):
            if minutes[i] > 0:
                min_diff = min(min_diff, i - first_pos)
                first_pos = i
        min_diff = min(min_diff, min_pos + (1440 - first_pos))
        return min_diff
# @lc code=end
