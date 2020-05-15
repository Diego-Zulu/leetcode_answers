/*
 * @lc app=leetcode id=75 lang=java
 *
 * [75] Sort Colors
 *
 * https://leetcode.com/problems/sort-colors/description/
 *
 * algorithms
 * Medium (45.37%)
 * Likes:    2829
 * Dislikes: 206
 * Total Accepted:    444.8K
 * Total Submissions: 979.8K
 * Testcase Example:  '[2,0,2,1,1,0]'
 *
 * Given an array with n objects colored red, white or blue, sort them in-place
 * so that objects of the same color are adjacent, with the colors in the order
 * red, white and blue.
 * 
 * Here, we will use the integers 0, 1, and 2 to represent the color red,
 * white, and blue respectively.
 * 
 * Note: You are not suppose to use the library's sort function for this
 * problem.
 * 
 * Example:
 * 
 * 
 * Input: [2,0,2,1,1,0]
 * Output: [0,0,1,1,2,2]
 * 
 * Follow up:
 * 
 * 
 * A rather straight forward solution is a two-pass algorithm using counting
 * sort.
 * First, iterate the array counting number of 0's, 1's, and 2's, then
 * overwrite array with total number of 0's, then 1's and followed by 2's.
 * Could you come up with a one-pass algorithm using only constant space?
 * 
 * 
 */

// @lc code=start
public class Solution {
    public void sortColors(int[] nums) {
        
        int p0 = 0, p2 = nums.length - 1, i = 0;
        
        while (i <= p2) {
            
            if (nums[i] == 0) {
                
                nums[i]=nums[p0];
                nums[p0]=0;
                p0++;
            } 
            if (nums[i] == 2) {
                nums[i]=nums[p2];
                nums[p2] = 2;
                p2--;
                i--;
            }
            i++;
        }
    }
}
// @lc code=end
