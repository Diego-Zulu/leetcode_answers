#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (76.28%)
# Likes:    967
# Dislikes: 34
# Total Accepted:    92.3K
# Total Submissions: 121.1K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# Return the root node of a binary search tree that matches the given preorder
# traversal.
# 
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of
# node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then
# traverses node.right.)
# 
# It's guaranteed that for the given test cases there is always possible to
# find a binary search tree with the given requirements.
# 
# Example 1:
# 
# 
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# The values of preorder are distinct.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from bisect import bisect_left

def bstFromPreorderAux(preorder, start, end):
    if start == end:
        return None
    curr = TreeNode(preorder[start])
    start += 1
    pos = bisect_left(preorder, curr.val, start, end)
    curr.left = bstFromPreorderAux(preorder, start, pos)
    curr.right = bstFromPreorderAux(preorder, pos, end)
    return curr

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return bstFromPreorderAux(preorder, 0, len(preorder))
# @lc code=end
