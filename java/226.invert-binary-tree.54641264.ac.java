/*
 * @lc app=leetcode id=226 lang=java
 *
 * [226] Invert Binary Tree
 *
 * https://leetcode.com/problems/invert-binary-tree/description/
 *
 * algorithms
 * Easy (62.65%)
 * Likes:    2871
 * Dislikes: 43
 * Total Accepted:    450.8K
 * Total Submissions: 719.1K
 * Testcase Example:  '[4,2,7,1,3,6,9]'
 *
 * Invert a binary tree.
 * 
 * Example:
 * 
 * Input:
 * 
 * 
 * ⁠    4
 * ⁠  /   \
 * ⁠ 2     7
 * ⁠/ \   / \
 * 1   3 6   9
 * 
 * Output:
 * 
 * 
 * ⁠    4
 * ⁠  /   \
 * ⁠ 7     2
 * ⁠/ \   / \
 * 9   6 3   1
 * 
 * Trivia:
 * This problem was inspired by this original tweet by Max Howell:
 * 
 * Google: 90% of our engineers use the software you wrote (Homebrew), but you
 * can’t invert a binary tree on a whiteboard so f*** off.
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
    public TreeNode invertTree(TreeNode root) {
        
        //recursiveInvertTree(root);
        //queueIterativeInvertTree(root);
        stackIterativeInvertTree(root);
        return root;
    }
    
    private void recursiveInvertTree(TreeNode root) {
        
        if (root != null && (root.left != null || root.right != null)) {
            TreeNode auxExchangeNode = root.left;
            root.left = root.right;
            root.right = auxExchangeNode;
            if (root.left != null)
                recursiveInvertTree(root.left);
            if (root.right != null)
                recursiveInvertTree(root.right);
        }
    }
    
    private void queueIterativeInvertTree(TreeNode root) {
        
        Queue<TreeNode> treeQueue = new LinkedList<>();
        if (root != null) treeQueue.add(root);
        
        while (!treeQueue.isEmpty()) {
            
            TreeNode actualNode = treeQueue.poll();
            TreeNode auxExchangeNode = actualNode.left;
            actualNode.left = actualNode.right;
            actualNode.right = auxExchangeNode;
            if (actualNode.left != null) treeQueue.add(actualNode.left);
            if (actualNode.right != null) treeQueue.add(actualNode.right);
        }
    }
    
    private void stackIterativeInvertTree(TreeNode root){
        
        Stack<TreeNode> treeStack = new Stack<>();
        
        if (root != null) treeStack.push(root);
        
        while (!treeStack.empty()) {
            
            TreeNode actualNode = treeStack.pop();
            TreeNode auxExchangeNode = actualNode.left;
            actualNode.left = actualNode.right;
            actualNode.right = auxExchangeNode;
            if (actualNode.left != null) treeStack.push(actualNode.left);
            if (actualNode.right != null) treeStack.push(actualNode.right);
        }
    }
}
// @lc code=end
