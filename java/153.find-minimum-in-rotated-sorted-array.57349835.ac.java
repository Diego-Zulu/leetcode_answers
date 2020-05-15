/*
 * @lc app=leetcode id=153 lang=java
 *
 * [153] Find Minimum in Rotated Sorted Array
 *
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (44.49%)
 * Likes:    1857
 * Dislikes: 218
 * Total Accepted:    410.8K
 * Total Submissions: 923.1K
 * Testcase Example:  '[3,4,5,1,2]'
 *
 * Suppose an array sorted in ascending order is rotated at some pivot unknown
 * to you beforehand.
 * 
 * (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
 * 
 * Find the minimum element.
 * 
 * You may assume no duplicate exists in the array.
 * 
 * Example 1:
 * 
 * 
 * Input: [3,4,5,1,2] 
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [4,5,6,7,0,1,2]
 * Output: 0
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int findMin(int[] nums) {
        
        int n=nums.length, l=0,r=n-1,m=n/2;
        
        while(true){
            
            if(l==m || m==r){
                return nums[l] < nums[r] ? nums[l] : nums[r];
            }
            else if (nums[l] > nums[m]){
                
                r=m;
            } else if (nums[m] > nums[r]){
                l=m;
            } else {
                return nums[l];
            }
            m=l+((r-l)/2);
        }
    }
}
// @lc code=end
