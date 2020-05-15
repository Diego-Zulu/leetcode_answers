/*
 * @lc app=leetcode id=283 lang=java
 *
 * [283] Move Zeroes
 *
 * https://leetcode.com/problems/move-zeroes/description/
 *
 * algorithms
 * Easy (57.30%)
 * Likes:    3497
 * Dislikes: 116
 * Total Accepted:    785.4K
 * Total Submissions: 1.4M
 * Testcase Example:  '[0,1,0,3,12]'
 *
 * Given an array nums, write a function to move all 0's to the end of it while
 * maintaining the relative order of the non-zero elements.
 * 
 * Example:
 * 
 * 
 * Input: [0,1,0,3,12]
 * Output: [1,3,12,0,0]
 * 
 * Note:
 * 
 * 
 * You must do this in-place without making a copy of the array.
 * Minimize the total number of operations.
 * 
 */

// @lc code=start
public class Solution {
    public void moveZeroes(int[] nums) {
        
        int[] result = new int[nums.length];
        int nextResultIndex = 0;
        
        for (int i=0; i<nums.length; i++) {
            
            if (nums[i] != 0) {
                result[nextResultIndex] = nums[i];
                nextResultIndex++;
            } 
        }
        
        for (int i=0; i<nextResultIndex; i++) {
            
            nums[i] = result[i];
        }
        
        for (int i = nextResultIndex; i<nums.length; i++) {
            
            nums[i] = 0;
        }
        
    }
}
// @lc code=end
