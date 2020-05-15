/*
 * @lc app=leetcode id=104 lang=java
 *
 * [104] Maximum Depth of Binary Tree
 *
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
 *
 * algorithms
 * Easy (64.95%)
 * Likes:    2245
 * Dislikes: 69
 * Total Accepted:    770.5K
 * Total Submissions: 1.2M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given a binary tree, find its maximum depth.
 * 
 * The maximum depth is the number of nodes along the longest path from the
 * root node down to the farthest leaf node.
 * 
 * Note: A leaf is a node with no children.
 * 
 * Example:
 * 
 * Given binary tree [3,9,20,null,null,15,7],
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * return its depth = 3.
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
    public int maxDepth(TreeNode root) {
        
        return recursiveMaxDepth(root);
        //return queueIterativeMaxDepth(root);
        //return stackIterativeMaxDepth(root);
    }
    
    private int recursiveMaxDepth(TreeNode root) {
        
        if (root == null) return 0;
        else return 1 + Math.max(recursiveMaxDepth(root.left),recursiveMaxDepth(root.right));
    }
    
    private int queueIterativeMaxDepth(TreeNode root) {
        
            Queue<TreeNode> queue = new LinkedList<>();
            int maxDepth = 0;
            if (root != null) queue.add(root);
            
            while (!queue.isEmpty()) {
                
                int queueSize = queue.size();
                for (int i=0; i<queueSize; i++) {
                    
                    TreeNode actualNode = queue.peek();
                    if (actualNode.left != null) queue.add(actualNode.left);
                    if (actualNode.right != null) queue.add(actualNode.right);
                    queue.remove();
                }
                
                maxDepth++;
            }
            
            return maxDepth;
    }
    
    private int stackIterativeMaxDepth(TreeNode root) {
        
        Stack<TreeNode> treeStack = new Stack<>();
        Stack<Integer> depthsStack = new Stack<>();
        int maxDepth = 0;
        
        if (root != null) {
            treeStack.push(root);
            depthsStack.push(1);
        }
        
        while (!treeStack.empty()) {
            
            int actualDepth = depthsStack.pop();
            TreeNode actualNode = treeStack.pop();
            
            if (actualNode.left == null && actualNode.right == null) {
                
                maxDepth = Math.max(maxDepth, actualDepth);
            } else {
                
                if (actualNode.right != null) {
                    depthsStack.push(1+actualDepth);
                    treeStack.push(actualNode.right);
                }
                
                if (actualNode.left != null) {
                    depthsStack.push(1+actualDepth);
                    treeStack.push(actualNode.left);
                }
            } 
        }
        
        return maxDepth;
    }
}
// @lc code=end
