/*
 * @lc app=leetcode id=33 lang=java
 *
 * [33] Search in Rotated Sorted Array
 *
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (34.23%)
 * Likes:    4507
 * Dislikes: 429
 * Total Accepted:    684.2K
 * Total Submissions: 2M
 * Testcase Example:  '[4,5,6,7,0,1,2]\n0'
 *
 * Suppose an array sorted in ascending order is rotated at some pivot unknown
 * to you beforehand.
 * 
 * (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
 * 
 * You are given a target value to search. If found in the array return its
 * index, otherwise return -1.
 * 
 * You may assume no duplicate exists in the array.
 * 
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [4,5,6,7,0,1,2], target = 3
 * Output: -1
 * 
 */

// @lc code=start
public class Solution {
    public int search(int[] nums, int target) {
        
        return searchRec(nums, 0, nums.length-1, target);
        
       /* for (int i=0; i<nums.length; i++) {
            
            if (nums[i] == target) return i;
        }
        return -1;*/
    }
    
    public int searchRec(int[] nums, int low, int high, int target) {
        if (low > high || high>=nums.length || low<0) {
            return -1;
        }
        int mid = (high - low)/2 + low;
        if (nums[mid] == target) return mid;
        else if (nums[mid] <= nums[high]) {//derecha ordenado
            if (target == nums[high]) {
                return high;
            } else if (target > nums[mid] && target <= nums[high]) {
                return searchRec(nums, mid+1, high, target);
            } else {
                return searchRec(nums, low, mid-1, target);
            }
        } else {
            if (target == nums[low]) {
                return low;
            } else if (target >= nums[low] && target < nums[mid]) {
                return searchRec(nums, low, mid-1, target);
            } else {
                return searchRec(nums, mid+1, high, target);
            }
        }
    }
}
// @lc code=end
