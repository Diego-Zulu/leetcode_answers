/*
 * @lc app=leetcode id=349 lang=java
 *
 * [349] Intersection of Two Arrays
 *
 * https://leetcode.com/problems/intersection-of-two-arrays/description/
 *
 * algorithms
 * Easy (60.89%)
 * Likes:    729
 * Dislikes: 1143
 * Total Accepted:    338.3K
 * Total Submissions: 555K
 * Testcase Example:  '[1,2,2,1]\n[2,2]'
 *
 * Given two arrays, write a function to compute their intersection.
 * 
 * Example 1:
 * 
 * 
 * Input: nums1 = [1,2,2,1], nums2 = [2,2]
 * Output: [2]
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
 * Output: [9,4]
 * 
 * 
 * Note:
 * 
 * 
 * Each element in the result must be unique.
 * The result can be in any order.
 * 
 * 
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        Map<Integer, Boolean> numbersInNums1 = new HashMap<>();
        Map<Integer, Boolean> intersectionNums = new HashMap<>();
        for (int number : nums1) {
            numbersInNums1.put(number, true);
        }
        
        for (int number : nums2) {
            if (numbersInNums1.get(number) != null && numbersInNums1.get(number)) {
                intersectionNums.put(number, true);
                numbersInNums1.put(number, false);
            }
        }
        int[] result = new int[intersectionNums.size()];
        int indexResult = 0;
        
        for (int number : nums2) {
            if (intersectionNums.get(number) != null && intersectionNums.get(number)) {
                result[indexResult] = number;
                indexResult++;
                intersectionNums.put(number, false);
            }
        }
        
        return result;
    }
}
// @lc code=end
