/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (45.32%)
 * Likes:    14642
 * Dislikes: 531
 * Total Accepted:    2.8M
 * Total Submissions: 6.3M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * Example:
 * 
 * 
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> present = new HashMap<>();
        
        for (int i=0; i<nums.length; i++) {
            
            if (present.containsKey(target - nums[i])) {
                
                return new int[] { present.get(target - nums[i]), i};
            }
             
            present.put(nums[i], i);
        }
        
        return null;
    }
}
// @lc code=end
