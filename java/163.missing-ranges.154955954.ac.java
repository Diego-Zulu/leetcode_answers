/*
 * @lc app=leetcode id=163 lang=java
 *
 * [163] Missing Ranges
 *
 * https://leetcode.com/problems/missing-ranges/description/
 *
 * algorithms
 * Medium (24.04%)
 * Likes:    312
 * Dislikes: 1772
 * Total Accepted:    80.9K
 * Total Submissions: 336.4K
 * Testcase Example:  '[0,1,3,50,75]\n0\n99'
 *
 * Given a sorted integer array nums, where the range of elements are in the
 * inclusive range [lower, upper], return its missing ranges.
 * 
 * Example:
 * 
 * 
 * Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
 * Output: ["2", "4->49", "51->74", "76->99"]
 * 
 * 
 */

// @lc code=start
class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        
        
        List<String> missingRanges = new LinkedList<>();
        for (int i=0; i<nums.length; i++) {
            
            if (lower < nums[i]) {
                
                StringBuilder range = new StringBuilder();
                range.append(lower);
                if (lower < nums[i] - 1) {
                    range.append("->");
                    range.append(nums[i] - 1);
                }
                missingRanges.add(range.toString());
            }
            lower = nums[i];
            if (lower < Integer.MAX_VALUE ) {
                lower++;
            }
        }
        
        if (lower <= upper && (nums.length == 0 || lower != nums[nums.length - 1]) ) {
            StringBuilder range = new StringBuilder();
            range.append(lower);
            if (lower < upper) {
                range.append("->");
                range.append(upper);
            }
            missingRanges.add(range.toString());
        }
        
        return missingRanges;
    }
}
// @lc code=end
