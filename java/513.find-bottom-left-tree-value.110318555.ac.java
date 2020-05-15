/*
 * @lc app=leetcode id=513 lang=java
 *
 * [513] Find Bottom Left Tree Value
 *
 * https://leetcode.com/problems/find-bottom-left-tree-value/description/
 *
 * algorithms
 * Medium (60.72%)
 * Likes:    813
 * Dislikes: 130
 * Total Accepted:    98.3K
 * Total Submissions: 161.8K
 * Testcase Example:  '[2,1,3]'
 *
 * 
 * Given a binary tree, find the leftmost value in the last row of the tree. 
 * 
 * 
 * Example 1:
 * 
 * Input:
 * 
 * ⁠   2
 * ⁠  / \
 * ⁠ 1   3
 * 
 * Output:
 * 1
 * 
 * 
 * 
 * ⁠ Example 2: 
 * 
 * Input:
 * 
 * ⁠       1
 * ⁠      / \
 * ⁠     2   3
 * ⁠    /   / \
 * ⁠   4   5   6
 * ⁠      /
 * ⁠     7
 * 
 * Output:
 * 7
 * 
 * 
 * 
 * Note:
 * You may assume the tree (i.e., the given root node) is not NULL.
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
public class Solution {
    
    public class LeftAndBottomNode {
        int val;
        int lev;
        LeftAndBottomNode(int value, int level) {val = value; lev = level;}
    }
    
    public int findBottomLeftValue(TreeNode root) {
        
        LeftAndBottomNode node = new LeftAndBottomNode(root.val, 1);
        findBottomLeftValueAux(root, node, 1);
        return node.val;
    }
    
    private void findBottomLeftValueAux(TreeNode root, LeftAndBottomNode chosenNode, int level) {
        
        if (chosenNode.lev < level) {
            chosenNode.lev = level;
            chosenNode.val = root.val;
        }
        if (root.left != null) {
            findBottomLeftValueAux(root.left, chosenNode, level+1);
        }
        if (root.right != null) {
            findBottomLeftValueAux(root.right, chosenNode, level+1);
        }
    }
}
// @lc code=end
