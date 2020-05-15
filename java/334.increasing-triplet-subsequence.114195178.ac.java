/*
 * @lc app=leetcode id=334 lang=java
 *
 * [334] Increasing Triplet Subsequence
 *
 * https://leetcode.com/problems/increasing-triplet-subsequence/description/
 *
 * algorithms
 * Medium (39.90%)
 * Likes:    1423
 * Dislikes: 124
 * Total Accepted:    135K
 * Total Submissions: 338.3K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * Given an unsorted array return whether an increasing subsequence of length 3
 * exists or not in the array.
 * 
 * Formally the function should:
 * 
 * Return true if there exists i, j, k 
 * such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return
 * false.
 * 
 * Note: Your algorithm should run in O(n) time complexity and O(1) space
 * complexity.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,3,4,5]
 * Output: true
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [5,4,3,2,1]
 * Output: false
 * 
 * 
 * 
 */

// @lc code=start
public class Solution {
    public boolean increasingTriplet(int[] nums) {
        
        int n = nums.length;
        
        if (n < 3) return false;
        
        int firstSmallest = Integer.MAX_VALUE;//MAX
        int secondSmallest = Integer.MAX_VALUE;//2
        
        for (int i : nums) {
            if (secondSmallest >= i) {
                secondSmallest = i;
            } else if (firstSmallest >= i) {
                firstSmallest = i;
            } else {
                return true;
            }
        }
        
        return false;
    }
}
// @lc code=end
