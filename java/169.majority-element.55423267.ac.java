/*
 * @lc app=leetcode id=169 lang=java
 *
 * [169] Majority Element
 *
 * https://leetcode.com/problems/majority-element/description/
 *
 * algorithms
 * Easy (57.79%)
 * Likes:    2921
 * Dislikes: 213
 * Total Accepted:    611.4K
 * Total Submissions: 1.1M
 * Testcase Example:  '[3,2,3]'
 *
 * Given an array of size n, find the majority element. The majority element is
 * the element that appears more than ⌊ n/2 ⌋ times.
 * 
 * You may assume that the array is non-empty and the majority element always
 * exist in the array.
 * 
 * Example 1:
 * 
 * 
 * Input: [3,2,3]
 * Output: 3
 * 
 * Example 2:
 * 
 * 
 * Input: [2,2,1,1,1,2,2]
 * Output: 2
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int majorityElement(int[] nums) {
        
        int count = 0;
        int major = 0;
        int n = nums.length;
        
        for (int i=0; i<n; i++) {
            
            if (count == 0) {
                major = nums[i];
            } 
            
            if (major == nums[i]) {
                count++;
            } else {
                count--;
            }
        }
        
        return major;
    }
}
// @lc code=end
