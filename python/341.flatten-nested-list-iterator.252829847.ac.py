#
# @lc app=leetcode id=341 lang=python
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (51.95%)
# Likes:    1522
# Dislikes: 618
# Total Accepted:    161.1K
# Total Submissions: 309.8K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, implement an iterator to flatten it.
# 
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
# 
# Example 1:
# 
# 
# 
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns
# false, 
# the order of elements returned by next should be: [1,1,2,1,1].
# 
# 
# Example 2:
# 
# 
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns
# false, 
# the order of elements returned by next should be: [1,4,6].
# 
# 
# 
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = [collections.deque(nestedList)]
        

    def next(self):
        self._clean_stack()
        return self.stack[-1].popleft().getInteger()
        

    def hasNext(self):
        self._clean_stack()
        return len(self.stack) > 0
    
    def _clean_stack(self):
        while self.stack:
            top = self.stack[-1]
            if not top:
                self.stack.pop()
                continue
            _next = top[0]
            if _next.isInteger():
                break
            else:
                top.popleft()
                self.stack.append(collections.deque(_next.getList()))
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
