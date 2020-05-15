#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#
# https://leetcode.com/problems/moving-average-from-data-stream/description/
#
# algorithms
# Easy (69.78%)
# Likes:    513
# Dislikes: 54
# Total Accepted:    113.9K
# Total Submissions: 163.2K
# Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
#
# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.
# 
# Example:
# 
# 
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
# 
# 
# 
# 
#

# @lc code=start
from collections import deque

class MovingAverage:

    def __init__(self, size: 'int'):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.sum = 0
        self.size = size

    def next(self, val: 'int') -> 'float':
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.size:
            self.sum -= self.q.popleft()
        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end
