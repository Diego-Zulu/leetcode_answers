/*
 * @lc app=leetcode id=560 lang=java
 *
 * [560] Subarray Sum Equals K
 *
 * https://leetcode.com/problems/subarray-sum-equals-k/description/
 *
 * algorithms
 * Medium (43.75%)
 * Likes:    4183
 * Dislikes: 133
 * Total Accepted:    285.5K
 * Total Submissions: 652.3K
 * Testcase Example:  '[1,1,1]\n2'
 *
 * Given an array of integers and an integer k, you need to find the total
 * number of continuous subarrays whose sum equals to k.
 * 
 * Example 1:
 * 
 * 
 * Input:nums = [1,1,1], k = 2
 * Output: 2
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The length of the array is in range [1, 20,000].
 * The range of numbers in the array is [-1000, 1000] and the range of the
 * integer k is [-1e7, 1e7].
 * 
 * 
 */

// @lc code=start
class Solution {
    public int subarraySum(int[] nums, int k) {
        
        HashMap<Integer, Integer> leftSums = new HashMap<>();
        leftSums.put(0, 1);
        int sum=0, count=0;        
        
        for (int i=0; i<nums.length; i++) {
            sum+=nums[i];
            if (leftSums.containsKey(sum - k)) {
                count += leftSums.get(sum - k);
            }
            leftSums.put(sum, leftSums.getOrDefault(sum, 0) + 1);
        }
        
        return count;
    }
}
// @lc code=end
