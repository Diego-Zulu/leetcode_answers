/*
 * @lc app=leetcode id=80 lang=java
 *
 * [80] Remove Duplicates from Sorted Array II
 *
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
 *
 * algorithms
 * Medium (43.12%)
 * Likes:    1016
 * Dislikes: 680
 * Total Accepted:    252.4K
 * Total Submissions: 585K
 * Testcase Example:  '[1,1,1,2,2,3]'
 *
 * Given a sorted array nums, remove the duplicates in-place such that
 * duplicates appeared at most twice and return the new length.
 * 
 * Do not allocate extra space for another array, you must do this by modifying
 * the input array in-place with O(1) extra memory.
 * 
 * Example 1:
 * 
 * 
 * Given nums = [1,1,1,2,2,3],
 * 
 * Your function should return length = 5, with the first five elements of nums
 * being 1, 1, 2, 2 and 3 respectively.
 * 
 * It doesn't matter what you leave beyond the returned length.
 * 
 * Example 2:
 * 
 * 
 * Given nums = [0,0,1,1,1,1,2,3,3],
 * 
 * Your function should return length = 7, with the first seven elements of
 * nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
 * 
 * It doesn't matter what values are set beyond the returned length.
 * 
 * 
 * Clarification:
 * 
 * Confused why the returned value is an integer but your answer is an array?
 * 
 * Note that the input array is passed in by reference, which means
 * modification to the input array will be known to the caller as well.
 * 
 * Internally you can think of this:
 * 
 * 
 * // nums is passed in by reference. (i.e., without making a copy)
 * int len = removeDuplicates(nums);
 * 
 * // any modification to nums in your function would be known by the caller.
 * // using the length returned by your function, it prints the first len
 * elements.
 * for (int i = 0; i < len; i++) {
 * print(nums[i]);
 * }
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int removeDuplicates(int[] nums) {
        
        int n = nums.length;
        
        if (n == 0) {
            return 0;
        }
        
        int repeatedTimes = 1;
        int length = 1;
        int insertInto = 1;
        
        for (int i=1; i<n; i++) {
            
            if (nums[i] == nums[i-1]) {
                if (repeatedTimes < 2) {
                    length++;
                    repeatedTimes++;
                    nums[insertInto] = nums[i];
                    insertInto++;
                } 
            } else {
                repeatedTimes = 1;
                length++;
                nums[insertInto] = nums[i];
                insertInto++;
            }
        }
        
        return length;
    }
}
// @lc code=end
