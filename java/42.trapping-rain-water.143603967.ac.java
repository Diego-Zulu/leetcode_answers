/*
 * @lc app=leetcode id=42 lang=java
 *
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (47.69%)
 * Likes:    6376
 * Dislikes: 111
 * Total Accepted:    476.5K
 * Total Submissions: 998.8K
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it is able to trap after raining.
 * 
 * 
 * The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 * In this case, 6 units of rain water (blue section) are being trapped. Thanks
 * Marcos for contributing this image!
 * 
 * Example:
 * 
 * 
 * Input: [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * 
 */

// @lc code=start
class Solution {
    public int trap(int[] height) {
        
        int l = findFirstLeftWall(height);
        int r = findFirstRightWall(height);
        
        int ans = 0;
        
        while (l < r) {
            
            int left = height[l];
            int right = height[r];
            
            if (left <= right) {
                
                while (l < r && left >= height[++l]) {
                    ans += left - height[l];
                }
            } else {
                while (l < r && right >= height[--r]) {
                    ans += right - height[r];
                }
            }
        }
        
        return ans;
    }
    
    public int findFirstLeftWall (int[] height) {
        
        for (int i=0; i<height.length - 1; i++) {
            
            if (height[i+1] < height[i]) {
                return i;
            }
        }
        
        return height.length;
    }
    
    public int findFirstRightWall (int[] height) {
        
        for (int i=height.length - 1; i > 0; i--) {
            
            if (height[i-1] < height[i]) {
                return i;
            }
        }
        
        return -1;
    }
}
// @lc code=end
