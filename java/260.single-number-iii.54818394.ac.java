/*
 * @lc app=leetcode id=260 lang=java
 *
 * [260] Single Number III
 *
 * https://leetcode.com/problems/single-number-iii/description/
 *
 * algorithms
 * Medium (60.31%)
 * Likes:    1296
 * Dislikes: 94
 * Total Accepted:    132.7K
 * Total Submissions: 219.9K
 * Testcase Example:  '[1,2,1,3,2,5]'
 *
 * Given an array of numbers nums, in which exactly two elements appear only
 * once and all the other elements appear exactly twice. Find the two elements
 * that appear only once.
 * 
 * Example:
 * 
 * 
 * Input:  [1,2,1,3,2,5]
 * Output: [3,5]
 * 
 * Note:
 * 
 * 
 * The order of the result is not important. So in the above example, [5, 3] is
 * also correct.
 * Your algorithm should run in linear runtime complexity. Could you implement
 * it using only constant space complexity?
 * 
 */

// @lc code=start
public class Solution {
    public int[] singleNumber(int[] nums) {
        

    int A = 0;  
    int B = 0;  
    int AXORB = 0;  
    for(int i = 0; i<nums.length; i++){  
        AXORB ^= nums[i];  
    }  

    AXORB = (AXORB & (AXORB - 1)) ^ AXORB; //find the different bit  in A and B
    for(int i = 0; i<nums.length; i++){  
        if((AXORB & nums[i]) == 0)  
            A ^= nums[i];  
        else  
            B ^= nums[i];  
    }  
    return new int[]{A, B};  

    }
}
// @lc code=end
