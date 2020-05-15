/*
 * @lc app=leetcode id=88 lang=java
 *
 * [88] Merge Sorted Array
 *
 * https://leetcode.com/problems/merge-sorted-array/description/
 *
 * algorithms
 * Easy (38.73%)
 * Likes:    1961
 * Dislikes: 3902
 * Total Accepted:    548.5K
 * Total Submissions: 1.4M
 * Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
 *
 * Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
 * one sorted array.
 * 
 * Note:
 * 
 * 
 * The number of elements initialized in nums1 and nums2 are m and n
 * respectively.
 * You may assume that nums1 has enough space (size that is greater or equal to
 * m + n) to hold additional elements from nums2.
 * 
 * 
 * Example:
 * 
 * 
 * Input:
 * nums1 = [1,2,3,0,0,0], m = 3
 * nums2 = [2,5,6],       n = 3
 * 
 * Output: [1,2,2,3,5,6]
 * 
 */

// @lc code=start
public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int n1 = m-1;
        int n2 = n-1;
        int i = n+m-1;
        while (i>=0 && n1>=0 && n2>=0) {
            if (nums1[n1] <= nums2[n2]) {
                
                nums1[i] = nums2[n2];
                n2--;
            } else {
                nums1[i] = nums1[n1];
                n1--;
            }
            i--;
        }
        
        while (n2>=0) {
            nums1[i] = nums2[n2];
            i--;
            n2--;
        }
    }
}
// @lc code=end
