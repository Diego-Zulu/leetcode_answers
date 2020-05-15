#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (35.60%)
# Likes:    1637
# Dislikes: 107
# Total Accepted:    217.1K
# Total Submissions: 609.1K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# Example 1:
# 
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = head
        end = head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        if not mid or not mid.next:
            return
        p1, p2 = mid.next, mid.next.next
        p1.next, mid.next = None, None
        
        while p2:
            p2.next, p2, p1 = p1, p2.next, p2
        head2 = p1
        while head2:
            head.next, head, head2.next, head2 = head2, head.next, head.next, head2.next
            
# @lc code=end
