/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 *
 * https://leetcode.com/problems/3sum/description/
 *
 * algorithms
 * Medium (26.07%)
 * Likes:    6310
 * Dislikes: 760
 * Total Accepted:    856K
 * Total Submissions: 3.3M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the
 * sum of zero.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate triplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [-1, 0, 1, 2, -1, -4],
 * 
 * A solution set is:
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 * 
 * 
 */

// @lc code=start
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> result = new LinkedList<>();
        int n = nums.length;
        int halfn = n/2;
        
        if (n < 3) return result;
        
        Arrays.sort(nums);
        int firstPointer = 1;
        int secondPointer = n - 1;
        
        for (int i=0; i < n;) {
            
            while (firstPointer < secondPointer) {
                int sum = nums[i] + nums[firstPointer] + nums[secondPointer];
                
                if (sum == 0) {
                    LinkedList<Integer> triplet = new LinkedList<>();
                    triplet.add(nums[i]);
                    triplet.add(nums[firstPointer]);
                    triplet.add(nums[secondPointer]);
                    result.add(triplet);
                    do {
                        firstPointer++;
                    } while (firstPointer < secondPointer && nums[firstPointer] == nums[firstPointer - 1]);
                    do {
                        secondPointer--;
                    } while (firstPointer < secondPointer && nums[secondPointer] == nums[secondPointer + 1]);
                    
                } else if (sum < 0) {
                    
                    do {
                        firstPointer++;
                    } while (firstPointer < secondPointer && nums[firstPointer] == nums[firstPointer - 1]);
                    
                } else if (sum > 0) {
                    do {
                        secondPointer--;
                    } while (firstPointer < secondPointer && nums[secondPointer] == nums[secondPointer + 1]);
                }
            }
            
             do {
                i++;
            } while (i < n && nums[i] == nums[i-1]);
            firstPointer = i + 1;
            secondPointer = n - 1;
        }
        
        return result;
    }
}
// @lc code=end
