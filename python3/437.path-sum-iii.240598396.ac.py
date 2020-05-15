#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (45.38%)
# Likes:    3078
# Dislikes: 248
# Total Accepted:    168.6K
# Total Submissions: 371.2K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
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


def pathSumAux(root, curr_sum, sum_starts, _sum):
    if root is None:
        return 0
    curr_sum += root.val
    paths = 0
    if curr_sum - _sum in sum_starts:
        paths += sum_starts[curr_sum - _sum]
    sum_starts[curr_sum] += 1
    paths += pathSumAux(root.left, curr_sum, sum_starts, _sum)
    paths += pathSumAux(root.right, curr_sum, sum_starts, _sum)
    sum_starts[curr_sum] -= 1
    return paths

class Solution:
    def pathSum(self, root: TreeNode, _sum: int) -> int:
        sum_starts = collections.defaultdict(int)
        sum_starts[0] = 1
        return pathSumAux(root, 0, sum_starts, _sum)
# @lc code=end
