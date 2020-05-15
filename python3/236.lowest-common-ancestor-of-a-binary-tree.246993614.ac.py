#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (43.91%)
# Likes:    3272
# Dislikes: 166
# Total Accepted:    432.4K
# Total Submissions: 983.8K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# 
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
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

def fillPathToFirst(root, target, path):
    if target == root:
        path.add(root)
        return True
    elif root is None:
        return False
    path.add(root)
    branches, found = [root.left, root.right], False
    while len(branches) and not found:
        found = fillPathToFirst(branches.pop(), target, path)
    if not found:
        path.remove(root)
    return found
    
def searchLowestInOtherPath(root, target, path, ancestor):
    if target == root:
        if len(ancestor) == 0 and root in path:
            ancestor.append(root)
        return True
    elif root is None:
        return False
    branches, found = [root.left, root.right], False
    while len(branches) and not found:
        found = searchLowestInOtherPath(branches.pop(), target, path, ancestor)
    if len(ancestor) == 0 and found and root in path:
        ancestor.append(root)
    return found

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        first_path, ancestor = set(), []
        fillPathToFirst(root, p, first_path)
        searchLowestInOtherPath(root, q, first_path, ancestor)
        return ancestor.pop()
# @lc code=end
