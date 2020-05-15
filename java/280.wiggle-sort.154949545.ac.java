/*
 * @lc app=leetcode id=280 lang=java
 *
 * [280] Wiggle Sort
 *
 * https://leetcode.com/problems/wiggle-sort/description/
 *
 * algorithms
 * Medium (63.18%)
 * Likes:    578
 * Dislikes: 56
 * Total Accepted:    81.9K
 * Total Submissions: 129.6K
 * Testcase Example:  '[3,5,2,1,6,4]'
 *
 * Given an unsorted array nums, reorder it in-place such that nums[0] <=
 * nums[1] >= nums[2] <= nums[3]....
 * 
 * Example:
 * 
 * 
 * Input: nums = [3,5,2,1,6,4]
 * Output: One possible answer is [3,5,1,6,2,4]
 * 
 */

// @lc code=start
class Solution {
    public void wiggleSort(int[] nums) {

        for (int i=0; i<nums.length - 1; i++) {
            
            if ((i & 1) == 1) {
                if (nums[i] < nums[i+1]) {
                    swap(nums, i, i+1);
                }
            } else {
                if (nums[i] > nums[i+1]) {
                    swap(nums, i, i+1);
                }
            }
        }
        
    }
    
    private void swap(int[] nums, int i, int j) {
        int aux = nums[i];
        nums[i] = nums[j];
        nums[j] = aux;
    }
}
// @lc code=end
