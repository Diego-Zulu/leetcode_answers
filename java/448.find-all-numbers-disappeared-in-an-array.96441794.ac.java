/*
 * @lc app=leetcode id=448 lang=java
 *
 * [448] Find All Numbers Disappeared in an Array
 *
 * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
 *
 * algorithms
 * Easy (55.58%)
 * Likes:    2547
 * Dislikes: 227
 * Total Accepted:    235.7K
 * Total Submissions: 423.9K
 * Testcase Example:  '[4,3,2,7,8,2,3,1]'
 *
 * Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
 * elements appear twice and others appear once.
 * 
 * Find all the elements of [1, n] inclusive that do not appear in this array.
 * 
 * Could you do it without extra space and in O(n) runtime? You may assume the
 * returned list does not count as extra space.
 * 
 * Example:
 * 
 * Input:
 * [4,3,2,7,8,2,3,1]
 * 
 * Output:
 * [5,6]
 * 
 * 
 */

// @lc code=start
public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        for (int i=0; i<nums.length; i++) {
            
            int actualNumb = Math.abs(nums[i]) - 1;
            
            if (nums[actualNumb] >= 0) {
                nums[actualNumb] = -nums[actualNumb];
            }
        }
        
        List<Integer> result = new LinkedList<>();
        
        for (int i=0; i<nums.length; i++) {
            
            if (nums[i] >= 0) {
                result.add(i+1);
            }
        }
        
        return result;
    }
}
// @lc code=end
