/*
 * @lc app=leetcode id=687 lang=java
 *
 * [687] Longest Univalue Path
 *
 * https://leetcode.com/problems/longest-univalue-path/description/
 *
 * algorithms
 * Easy (35.62%)
 * Likes:    1525
 * Dislikes: 420
 * Total Accepted:    85.6K
 * Total Submissions: 240K
 * Testcase Example:  '[5,4,5,1,1,5]'
 *
 * Given a binary tree, find the length of the longest path where each node in
 * the path has the same value. This path may or may not pass through the
 * root.
 * 
 * The length of path between two nodes is represented by the number of edges
 * between them.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input:
 * 
 * 
 * ⁠             5
 * ⁠            / \
 * ⁠           4   5
 * ⁠          / \   \
 * ⁠         1   1   5
 * 
 * 
 * Output: 2
 * 
 * 
 * 
 * Example 2:
 * 
 * Input:
 * 
 * 
 * ⁠             1
 * ⁠            / \
 * ⁠           4   5
 * ⁠          / \   \
 * ⁠         4   4   5
 * 
 * 
 * Output: 2
 * 
 * 
 * 
 * Note: The given binary tree has not more than 10000 nodes. The height of the
 * tree is not more than 1000.
 * 
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
    
    int maxLength;
    
    public int longestUnivaluePath(TreeNode root) {
        
        if (root == null) return 0;
        
        maxLength = 0;
        longestUnivaluePathRec(root, root.val);
        
        return maxLength;
    }
    
    private int longestUnivaluePathRec(TreeNode root, int lastNumber) {
        
        if (root == null) return 0;
        
        int left = longestUnivaluePathRec(root.left, root.val);
        int right = longestUnivaluePathRec(root.right, root.val);
        maxLength = Math.max(maxLength, left + right);
        
        if (root.val == lastNumber) return 1 + Math.max(left, right);
        return 0;
    }
}
// @lc code=end
