/*
 * @lc app=leetcode id=238 lang=java
 *
 * [238] Product of Array Except Self
 *
 * https://leetcode.com/problems/product-of-array-except-self/description/
 *
 * algorithms
 * Medium (59.23%)
 * Likes:    4421
 * Dislikes: 384
 * Total Accepted:    500.5K
 * Total Submissions: 844.7K
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an array nums of n integers where n > 1,  return an array output such
 * that output[i] is equal to the product of all the elements of nums except
 * nums[i].
 * 
 * Example:
 * 
 * 
 * Input:  [1,2,3,4]
 * Output: [24,12,8,6]
 * 
 * 
 * Constraint: It's guaranteed that the product of the elements of any prefix
 * or suffix of the array (including the whole array) fits in a 32 bit
 * integer.
 * 
 * Note: Please solve it without division and in O(n).
 * 
 * Follow up:
 * Could you solve it with constant space complexity? (The output array does
 * not count as extra space for the purpose of space complexity analysis.)
 * 
 */

// @lc code=start
public class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        int[] output = new int[nums.length];
        int totalProduct = 1;
        int partialProduct = 1;
        int numberOfZeroes = 0;
        
        for (int i=0; i<output.length; i++) {
            
            if (nums[i] != 0) totalProduct *= nums[i];
            else numberOfZeroes++;
        }
        
        if (numberOfZeroes > 1){
            partialProduct = 0;
            totalProduct = 0;
        } else if (numberOfZeroes == 1) {
            partialProduct = totalProduct;
            totalProduct = 0;
        }
        
        for (int i=0; i<output.length; i++) {
            
            if (nums[i] == 0) output[i] = partialProduct;
            else output[i] = totalProduct / nums[i];
        }
        
        return output;
    }
}
// @lc code=end
