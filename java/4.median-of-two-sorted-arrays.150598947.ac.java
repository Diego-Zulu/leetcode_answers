/*
 * @lc app=leetcode id=4 lang=java
 *
 * [4] Median of Two Sorted Arrays
 *
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (28.89%)
 * Likes:    6604
 * Dislikes: 1013
 * Total Accepted:    647.4K
 * Total Submissions: 2.2M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * 
 * Find the median of the two sorted arrays. The overall run time complexity
 * should be O(log (m+n)).
 * 
 * You may assume nums1 and nums2 cannot be both empty.
 * 
 * Example 1:
 * 
 * 
 * nums1 = [1, 3]
 * nums2 = [2]
 * 
 * The median is 2.0
 * 
 * 
 * Example 2:
 * 
 * 
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * 
 * The median is (2 + 3)/2 = 2.5
 * 
 * 
 */

// @lc code=start
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        if (nums1.length > nums2.length) {
            int[] temp = nums1; nums1 = nums2; nums2 = temp;
        }
        int m = nums1.length;
        int n = nums2.length;
        int imin = 0;
        int imax = m;
        int halfLength = (n + m + 1) / 2;
        
        while (imin <= imax) {
            
            int i = (imin + imax) / 2;
            int j = halfLength - i;
            
            if (i < imax && nums1[i] < nums2[j-1]) {
                imin++;
            } else if (i > imin && nums1[i - 1] > nums2[j]) {
                imax--;
            } else {
                
                int leftMax = 0;
                if (i == 0) leftMax = nums2[j-1];
                else if (j == 0) leftMax = nums1[i-1];
                else leftMax = Math.max(nums1[i-1], nums2[j-1]);
                
                if ((n + m) % 2 == 1) return leftMax;
                
                int rightMin = 0;
                if (i == m) rightMin = nums2[j];
                else if (j == n) rightMin = nums1[i];
                else rightMin = Math.min(nums1[i], nums2[j]);
                
                return (leftMax + rightMin) / 2d;
            }
        }
        
        return 0d;
    }
}
// @lc code=end
