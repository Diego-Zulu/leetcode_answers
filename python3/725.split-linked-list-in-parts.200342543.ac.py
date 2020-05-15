#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
# https://leetcode.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (51.27%)
# Likes:    567
# Dislikes: 111
# Total Accepted:    44.2K
# Total Submissions: 86.2K
# Testcase Example:  '[1,2,3,4]\n5'
#
# Given a (singly) linked list with head node root, write a function to split
# the linked list into k consecutive linked list "parts".
# 
# The length of each part should be as equal as possible: no two parts should
# have a size differing by more than 1.  This may lead to some parts being
# null.
# 
# The parts should be in order of occurrence in the input list, and parts
# occurring earlier should always have a size greater than or equal parts
# occurring later.
# 
# Return a List of ListNode's representing the linked list parts that are
# formed.
# 
# 
# Examples
# 1->2->3->4, k = 5 // 5 equal parts
# [ [1], 
# [2],
# [3],
# [4],
# null ]
# 
# Example 1:
# 
# Input: 
# root = [1, 2, 3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The input and each element of the output are ListNodes, not arrays.
# For example, the input root has root.val = 1, root.next.val = 2,
# \root.next.next.val = 3, and root.next.next.next = null.
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but it's string representation as a
# ListNode is [].
# 
# 
# 
# Example 2:
# 
# Input: 
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most
# 1, and earlier parts are a larger size than the later parts.
# 
# 
# 
# Note:
# The length of root will be in the range [0, 1000].
# Each value of a node in the input will be an integer in the range [0, 999].
# k will be an integer in the range [1, 50].
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        root_length = 0
        r = root
        while r:
            root_length += 1
            r = r.next
            
        part_size = int(root_length / k)
        bigger_parts = root_length % k
        r = root
        parts = []
        
        for i in range(k):
            current_size = part_size
            if bigger_parts > 0:
                bigger_parts -= 1
                current_size += 1
            
            current_part = None
            current_part_end = None
            for j in range(current_size):
                if r is None:
                    break
                else:
                    if current_part:
                        current_part_end.next = ListNode(r.val)
                        current_part_end = current_part_end.next
                    else:
                        current_part = ListNode(r.val)
                        current_part_end = current_part
                    r = r.next
                
            parts.append(current_part)
            
        return parts
        
# @lc code=end
