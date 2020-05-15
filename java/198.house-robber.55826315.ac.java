/*
 * @lc app=leetcode id=198 lang=java
 *
 * [198] House Robber
 *
 * https://leetcode.com/problems/house-robber/description/
 *
 * algorithms
 * Easy (41.72%)
 * Likes:    4301
 * Dislikes: 127
 * Total Accepted:    484.4K
 * Total Submissions: 1.2M
 * Testcase Example:  '[1,2,3,1]'
 *
 * You are a professional robber planning to rob houses along a street. Each
 * house has a certain amount of money stashed, the only constraint stopping
 * you from robbing each of them is that adjacent houses have security system
 * connected and it will automatically contact the police if two adjacent
 * houses were broken into on the same night.
 * 
 * Given a list of non-negative integers representing the amount of money of
 * each house, determine the maximum amount of money you can rob tonight
 * without alerting the police.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,3,1]
 * Output: 4
 * Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
 * 3).
 * Total amount you can rob = 1 + 3 = 4.
 * 
 * Example 2:
 * 
 * 
 * Input: [2,7,9,3,1]
 * Output: 12
 * Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house
 * 5 (money = 1).
 * Total amount you can rob = 2 + 9 + 1 = 12.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int rob(int[] nums) {
        
        int numsLength = nums.length;
        int[] treasure = new int[numsLength];
        int mayor = -1;
        
        if (numsLength < 1) return 0;
        else if (numsLength < 2) return nums[0];
        else if (numsLength == 2) {
            return nums[0] > nums[1] ? nums[0] : nums[1];

        } else {
            treasure[0] = nums[0];
            treasure[1] = nums[1];
            treasure[2] = nums[2] + nums[0];
            mayor = treasure[2] > treasure[1] ? treasure[2] : treasure[1];
        }
        
        for (int i=3; i<numsLength; i++) {
            
            treasure[i] = nums[i] + treasure[i-2] > nums[i] + treasure[i-3] ? nums[i] + treasure[i-2] : nums[i] + treasure[i-3];
            mayor = mayor > treasure[i] ? mayor : treasure[i];
            
        }
        
        return mayor;
    }
}
// @lc code=end
