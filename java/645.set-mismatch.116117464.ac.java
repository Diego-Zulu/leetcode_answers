/*
 * @lc app=leetcode id=645 lang=java
 *
 * [645] Set Mismatch
 *
 * https://leetcode.com/problems/set-mismatch/description/
 *
 * algorithms
 * Easy (41.79%)
 * Likes:    602
 * Dislikes: 287
 * Total Accepted:    68.7K
 * Total Submissions: 164.3K
 * Testcase Example:  '[1,2,2,4]'
 *
 * 
 * The set S originally contains numbers from 1 to n. But unfortunately, due to
 * the data error, one of the numbers in the set got duplicated to another
 * number in the set, which results in repetition of one number and loss of
 * another number. 
 * 
 * 
 * 
 * Given an array nums representing the data status of this set after the
 * error. Your task is to firstly find the number occurs twice and then find
 * the number that is missing. Return them in the form of an array.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [1,2,2,4]
 * Output: [2,3]
 * 
 * 
 * 
 * Note:
 * 
 * The given array size will in the range [2, 10000].
 * The given array's numbers won't have any order.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[] findErrorNums(int[] nums) {
        
        int[] result = new int[2];
        for (int i=0; i<nums.length; i++) {
            int pos = Math.abs(nums[i]) - 1;
            if (nums[pos] < 0) result[0] = pos + 1;
            else nums[pos] *= -1;
        }
        
        for (int i=0; i<nums.length; i++) {
            if (nums[i] > 0) {
                result[1] = i + 1;
                break;
            }
        }
        
        return result;
    }
}
// @lc code=end
