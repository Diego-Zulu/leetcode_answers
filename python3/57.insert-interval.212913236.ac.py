#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (32.96%)
# Likes:    1436
# Dislikes: 169
# Total Accepted:    235.8K
# Total Submissions: 715K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        res = []
        for i in intervals:
            if newInterval:
                if newInterval.end < i.start:
                    res.append(newInterval)
                    newInterval = None
                elif newInterval.start <= i.end:
                    newInterval = Interval(min(i.start, newInterval.start), max(i.end, newInterval.end))
                    continue
            res.append(i)
        if newInterval:
            res.append(newInterval)
        return res
# @lc code=end
