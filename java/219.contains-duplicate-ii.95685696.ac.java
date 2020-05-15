/*
 * @lc app=leetcode id=219 lang=java
 *
 * [219] Contains Duplicate II
 *
 * https://leetcode.com/problems/contains-duplicate-ii/description/
 *
 * algorithms
 * Easy (37.17%)
 * Likes:    769
 * Dislikes: 926
 * Total Accepted:    257.8K
 * Total Submissions: 693.2K
 * Testcase Example:  '[1,2,3,1]\n3'
 *
 * Given an array of integers and an integer k, find out whether there are two
 * distinct indices i and j in the array such that nums[i] = nums[j] and the
 * absolute difference between i and j is at most k.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,3,1], k = 3
 * Output: true
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,0,1,1], k = 1
 * Output: true
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,2,3,1,2,3], k = 2
 * Output: false
 * 
 * 
 * 
 * 
 * 
 */

// @lc code=start
public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        
        Set<Integer> numbersInArray = new HashSet<Integer>();
        
        for (int i=0; i < nums.length; i++) {
            
            if (i > k) {
                numbersInArray.remove(nums[i-k-1]);
            }
            
            if (!numbersInArray.add(nums[i])) {
                return true;
            }
        }
        
        return false;
    }
}
// @lc code=end
