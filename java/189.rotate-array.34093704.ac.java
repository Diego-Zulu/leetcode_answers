/*
 * @lc app=leetcode id=189 lang=java
 *
 * [189] Rotate Array
 *
 * https://leetcode.com/problems/rotate-array/description/
 *
 * algorithms
 * Easy (33.75%)
 * Likes:    2482
 * Dislikes: 778
 * Total Accepted:    456.3K
 * Total Submissions: 1.4M
 * Testcase Example:  '[1,2,3,4,5,6,7]\n3'
 *
 * Given an array, rotate the array to the right by k steps, where k is
 * non-negative.
 * 
 * Follow up:
 * 
 * 
 * Try to come up as many solutions as you can, there are at least 3 different
 * ways to solve this problem.
 * Could you do it in-place with O(1) extra space?
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,3,4,5,6,7], k = 3
 * Output: [5,6,7,1,2,3,4]
 * Explanation:
 * rotate 1 steps to the right: [7,1,2,3,4,5,6]
 * rotate 2 steps to the right: [6,7,1,2,3,4,5]
 * rotate 3 steps to the right: [5,6,7,1,2,3,4]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [-1,-100,3,99], k = 2
 * Output: [3,99,-1,-100]
 * Explanation: 
 * rotate 1 steps to the right: [99,-1,-100,3]
 * rotate 2 steps to the right: [3,99,-1,-100]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 2 * 10^4
 * It's guaranteed that nums[i] fits in a 32 bit-signed integer.
 * k >= 0
 * 
 * 
 */

// @lc code=start
public class Solution {
    public void rotate(int[] nums, int k) {
        
        int [] nuevo = new int[nums.length*2];
        if (k>nums.length) k=k-nums.length;
            if(k!=0 && nums.length>1){
                for(int i=0; i<nums.length; i++){
                        nuevo[i] = nums[i];
                        nuevo[i+nums.length] = nums[i];
                }
                
                int j = 0;
                /*int contarAca = 0;
                if (nums.length%2 == 0) {
                    contarAca = k;
                } else contarAca = k+1;*/
                for(int i=nums.length-k; j<nums.length; i++){
                      nums[j] = nuevo[i];
                      j++;
                }
            }
       /* if(k!=0 && nums.length>1){
            for(int i=0; i<=k; i++){
                nuevo[k+i-1] = nums[i];
            }
            for(int i=k+1; i<nums.length; i++){
                nuevo[i-k-1] = nums[i];
            }
            for(int i=0; i<nuevo.length; i++){
                nums[i] = nuevo[i];
            } */
    }
}
// @lc code=end
