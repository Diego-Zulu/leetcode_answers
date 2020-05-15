/*
 * @lc app=leetcode id=78 lang=java
 *
 * [78] Subsets
 *
 * https://leetcode.com/problems/subsets/description/
 *
 * algorithms
 * Medium (59.33%)
 * Likes:    3282
 * Dislikes: 77
 * Total Accepted:    526.5K
 * Total Submissions: 886.7K
 * Testcase Example:  '[1,2,3]'
 *
 * Given a set of distinct integers, nums, return all possible subsets (the
 * power set).
 * 
 * Note: The solution set must not contain duplicate subsets.
 * 
 * Example:
 * 
 * 
 * Input: nums = [1,2,3]
 * Output:
 * [
 * ⁠ [3],
 * [1],
 * [2],
 * [1,2,3],
 * [1,3],
 * [2,3],
 * [1,2],
 * []
 * ]
 * 
 */

// @lc code=start
public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new LinkedList<>();
        subsetsRecursion(nums, 0, new LinkedList<Integer>(), result);
        
        return result;
    }
    
    private void subsetsRecursion(int[] nums, int pos, 
                                  List<Integer> actualList, List<List<Integer>> result) {
        
        if (pos < nums.length) {
            subsetsRecursion(nums, pos+1, actualList, result);
            actualList.add(nums[pos]);
            subsetsRecursion(nums, pos+1, actualList, result);
            actualList.remove(actualList.size() - 1);
        } else {
            result.add(new LinkedList<Integer>(actualList));
        }
    }
}
// @lc code=end
