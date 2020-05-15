/*
 * @lc app=leetcode id=217 lang=java
 *
 * [217] Contains Duplicate
 *
 * https://leetcode.com/problems/contains-duplicate/description/
 *
 * algorithms
 * Easy (55.44%)
 * Likes:    768
 * Dislikes: 689
 * Total Accepted:    526.8K
 * Total Submissions: 949.9K
 * Testcase Example:  '[1,2,3,1]'
 *
 * Given an array of integers, find if the array contains any duplicates.
 * 
 * Your function should return true if any value appears at least twice in the
 * array, and it should return false if every element is distinct.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,3,1]
 * Output: true
 * 
 * Example 2:
 * 
 * 
 * Input: [1,2,3,4]
 * Output: false
 * 
 * Example 3:
 * 
 * 
 * Input: [1,1,1,3,3,4,3,2,4,2]
 * Output: true
 * 
 */

// @lc code=start
public class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        //return containsDuplicateImplementedWithHashMap(nums);
        return containsDuplicateImplementedWithBitSet(nums);
    }
    
    private boolean containsDuplicateImplementedWithHashMap(int[] nums){
        
        HashMap repeatedNumbers = new HashMap();
        
        for (int i=0; i<nums.length; i++) {
            
            if (repeatedNumbers.get(nums[i]) == null)
            repeatedNumbers.put(nums[i], 1);
            else return true;
        }
        
        return false;
    }
    
    private boolean containsDuplicateImplementedWithBitSet(int[] nums) {
        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for (int i=0; i<nums.length; i++) {
            
            if (min > nums[i]) min = nums[i];
            if (max < nums[i]) max = nums[i];
        }
        
        int diference = max - min + 1;
        BitSet repeated = new BitSet(diference);
        
         for (int i=0; i<nums.length; i++) {
            
            if (!repeated.get(nums[i] - min)) repeated.set(nums[i] - min);
            else return true;
        }
        
        return false;
    }
}
// @lc code=end
