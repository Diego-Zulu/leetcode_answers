#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (39.15%)
# Likes:    4275
# Dislikes: 271
# Total Accepted:    605.7K
# Total Submissions: 1.5M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import deque

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = deque(filter(None, lists if lists is not None else []))
        if not lists:
            return None
        
        while len(lists) > 1:
            l1 = lists.popleft()
            l2 = lists.popleft()
            head = l1 if l1.val < l2.val else l2
            other = l2 if l1.val < l2.val else l1
            l1 = head
            while other:
                while head.next and head.next.val < other.val:
                    head = head.next
                l = ListNode(other.val)
                l.next = head.next
                head.next = l
                other = other.next
            lists.append(l1)
        return lists.popleft()
        
# @lc code=end
