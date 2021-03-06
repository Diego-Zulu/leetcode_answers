/*
 * @lc app=leetcode id=654 lang=java
 *
 * [654] Maximum Binary Tree
 *
 * https://leetcode.com/problems/maximum-binary-tree/description/
 *
 * algorithms
 * Medium (79.04%)
 * Likes:    1625
 * Dislikes: 220
 * Total Accepted:    123.7K
 * Total Submissions: 156.5K
 * Testcase Example:  '[3,2,1,6,0,5]'
 *
 * 
 * Given an integer array with no duplicates. A maximum tree building on this
 * array is defined as follow:
 * 
 * The root is the maximum number in the array. 
 * The left subtree is the maximum tree constructed from left part subarray
 * divided by the maximum number.
 * The right subtree is the maximum tree constructed from right part subarray
 * divided by the maximum number. 
 * 
 * 
 * 
 * 
 * Construct the maximum tree by the given array and output the root node of
 * this tree.
 * 
 * 
 * Example 1:
 * 
 * Input: [3,2,1,6,0,5]
 * Output: return the tree root node representing the following tree:
 * 
 * ⁠     6
 * ⁠   /   \
 * ⁠  3     5
 * ⁠   \    / 
 * ⁠    2  0   
 * ⁠      \
 * ⁠       1
 * 
 * 
 * 
 * Note:
 * 
 * The size of the given array will be in the range [1,1000].
 * 
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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        
        return constructMaxRecursively(nums, 0, nums.length - 1);
    }
    
    private TreeNode constructMaxRecursively(int[] nums, int from, int till) {
        
        TreeNode maxActualNode = null;
        if (from <= till) {
            
            int maxPos = findMaxPosWithinRange(nums, from, till);
            maxActualNode = new TreeNode(nums[maxPos]);
            maxActualNode.left = constructMaxRecursively(nums, from, maxPos - 1);
            maxActualNode.right = constructMaxRecursively(nums, maxPos + 1, till);
        }
        return maxActualNode;
    }
    
    private int findMaxPosWithinRange(int[] nums, int from, int till) {
        
        int max = nums[from];
        int pos = from;
        
        for (int i=from+1; i<=till; i++) {
            
            if (max < nums[i]) {
                max = nums[i]; 
                pos = i;
            }
        }
        
        return pos;
    }
}
// @lc code=end
