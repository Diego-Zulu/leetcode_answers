/*
 * @lc app=leetcode id=298 lang=java
 *
 * [298] Binary Tree Longest Consecutive Sequence
 *
 * https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
 *
 * algorithms
 * Medium (46.59%)
 * Likes:    484
 * Dislikes: 116
 * Total Accepted:    80.2K
 * Total Submissions: 172.1K
 * Testcase Example:  '[1,null,3,2,4,null,null,null,5]'
 *
 * Given a binary tree, find the length of the longest consecutive sequence
 * path.
 * 
 * The path refers to any sequence of nodes from some starting node to any node
 * in the tree along the parent-child connections. The longest consecutive path
 * need to be from parent to child (cannot be the reverse).
 * 
 * Example 1:
 * 
 * 
 * Input:
 * 
 * ⁠  1
 * ⁠   \
 * ⁠    3
 * ⁠   / \
 * ⁠  2   4
 * ⁠       \
 * ⁠        5
 * 
 * Output: 3
 * 
 * Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
 * 
 * Example 2:
 * 
 * 
 * Input:
 * 
 * ⁠  2
 * ⁠   \
 * ⁠    3
 * ⁠   / 
 * ⁠  2    
 * ⁠ / 
 * ⁠1
 * 
 * Output: 2 
 * 
 * Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return
 * 2.
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int longestConsecutive(TreeNode root) {
        
        return longestConsecutiveRecursive(root, null, 0);
    }
    
    private int longestConsecutiveRecursive(TreeNode root, Integer lastNumber, int sequenceLength) {
        
        if (root == null) return sequenceLength;
        
        if (lastNumber != null && lastNumber + 1 == root.val) sequenceLength++;
        else {
            sequenceLength = 1;
        }
        
        return Math.max(sequenceLength, Math.max(
            longestConsecutiveRecursive(root.left, root.val, sequenceLength), 
            longestConsecutiveRecursive(root.right, root.val, sequenceLength)));
    }
}
// @lc code=end
