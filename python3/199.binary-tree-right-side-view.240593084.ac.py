#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (52.74%)
# Likes:    1951
# Dislikes: 117
# Total Accepted:    264K
# Total Submissions: 500.2K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        right_view = []
        dfs = [(root, 0)]
        while len(dfs) > 0:
            curr_node, curr_level = dfs.pop()
            if curr_level == len(right_view):
                right_view.append(curr_node.val)
            if curr_node.left is not None:
                dfs.append((curr_node.left, curr_level + 1))
            if curr_node.right is not None:
                dfs.append((curr_node.right, curr_level + 1))
        return right_view
# @lc code=end
