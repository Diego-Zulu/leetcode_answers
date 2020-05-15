#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (45.16%)
# Likes:    2396
# Dislikes: 41
# Total Accepted:    268.8K
# Total Submissions: 595.1K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
# 
# Example 1:
# 
# 
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: 1
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
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        end_intervals = sorted([i.end for i in intervals])
        start_intervals = sorted([i.start for i in intervals])
        n = len(intervals)
        start_pos, end_pos, rooms = 0, 0, 0
        while start_pos < n:
            if start_intervals[start_pos] >= end_intervals[end_pos]:
                rooms -= 1
                end_pos += 1
            rooms += 1
            start_pos += 1
        return rooms
        
# @lc code=end
