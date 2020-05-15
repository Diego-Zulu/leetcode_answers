#
# @lc app=leetcode id=681 lang=python3
#
# [681] Next Closest Time
#
# https://leetcode.com/problems/next-closest-time/description/
#
# algorithms
# Medium (44.54%)
# Likes:    449
# Dislikes: 693
# Total Accepted:    60.7K
# Total Submissions: 136.3K
# Testcase Example:  '"19:34"'
#
# Given a time represented in the format "HH:MM", form the next closest time by
# reusing the current digits. There is no limit on how many times a digit can
# be reused.
# 
# You may assume the given input string is always valid. For example, "01:34",
# "12:09" are all valid. "1:34", "12:9" are all invalid.
# 
# Example 1:
# 
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours
# and 59 minutes later.
# 
# 
# 
# Example 2:
# 
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is
# smaller than the input time numerically.
# 
# 
#

# @lc code=start
def withinLimit(time, number, pos):
    if pos == 3:
        return number <= '9'
    if pos == 2:
        return number <= '5'
    if pos == 1:
        return (time[0] <= '1' and number <= '9') or (time[0] == '2' and number <= '3')
    if pos == 0:
        return number <= '2'


class Solution:
    def nextClosestTime(self, time: str) -> str:
        time = [time[0], time[1], time[3], time[4]]
        availableDigits = sorted(time)
        next_time = []
        i = 3
        while i >= 0:
            for d in availableDigits:
                if d > time[i] and withinLimit(time, d, i):
                    next_time = time[0:i] + [d]
                    i = 0
                    break
            i -= 1
        while len(next_time) < 4:
            next_time.append(availableDigits[0])
        return ''.join(next_time[0:2] + [':'] + next_time[2:4])
# @lc code=end
