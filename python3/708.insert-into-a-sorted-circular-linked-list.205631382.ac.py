#
# @lc app=leetcode id=708 lang=python3
#
# [708] Insert into a Sorted Circular Linked List
#
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/
#
# algorithms
# Medium (31.27%)
# Likes:    269
# Dislikes: 283
# Total Accepted:    32K
# Total Submissions: 102.5K
# Testcase Example:  '[3,4,1]\n2'
#
# Given a node from a Circular Linked List which is sorted in ascending order,
# write a function to insert a value insertVal into the list such that it
# remains a sorted circular list. The given node can be a reference to any
# single node in the list, and may not be necessarily the smallest value in the
# circular list.
# 
# If there are multiple suitable places for insertion, you may choose any place
# to insert the new value. After the insertion, the circular list should remain
# sorted.
# 
# If the list is empty (i.e., given node is null), you should create a new
# single circular list and return the reference to that single node. Otherwise,
# you should return the original given node.
# 
# 
# Example 1:
# 
# 
# 
# Input: head = [3,4,1], insertVal = 2
# Output: [3,4,1,2]
# Explanation: In the figure above, there is a sorted circular list of three
# elements. You are given a reference to the node with value 3, and we need to
# insert 2 into the list. The new node should be inserted between node 1 and
# node 3. After the insertion, the list should look like this, and we should
# still return node 3.
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = [], insertVal = 1
# Output: [1]
# Explanation: The list is empty (given head is null). We create a new single
# circular list and return the reference to that single node.
# 
# 
# Example 3:
# 
# 
# Input: head = [1], insertVal = 0
# Output: [1,0]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= Number of Nodes <= 5 * 10^4
# -10^6 <= Node.val <= 10^6
# -10^6 <= insertVal <= 10^6
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: 'int') -> 'Node':
        if head is None:
            head = Node(insertVal, None)
            head.next = head
            return head
        
        iter_node = head
        tipping_point_passed = False
        while iter_node:
            
            if (not tipping_point_passed and (head.val > iter_node.next.val or iter_node.next == head) and \
                ((iter_node.val >= insertVal and insertVal <= iter_node.next.val) or \
                (iter_node.val <= insertVal and iter_node.next.val <= insertVal))) or \
               (iter_node.val <= insertVal and insertVal <= iter_node.next.val):
                iter_node.next = Node(insertVal, iter_node.next)
                iter_node = None
                break
            elif not tipping_point_passed and (head.val > iter_node.next.val or iter_node.next == head):
                tipping_point_passed = True
            iter_node = iter_node.next
        
        return head
                
# @lc code=end
