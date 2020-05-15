/*
 * @lc app=leetcode id=605 lang=java
 *
 * [605] Can Place Flowers
 *
 * https://leetcode.com/problems/can-place-flowers/description/
 *
 * algorithms
 * Easy (31.58%)
 * Likes:    726
 * Dislikes: 345
 * Total Accepted:    95.7K
 * Total Submissions: 303K
 * Testcase Example:  '[1,0,0,0,1]\n1'
 *
 * Suppose you have a long flowerbed in which some of the plots are planted and
 * some are not. However, flowers cannot be planted in adjacent plots - they
 * would compete for water and both would die.
 * 
 * Given a flowerbed (represented as an array containing 0 and 1, where 0 means
 * empty and 1 means not empty), and a number n, return if n new flowers can be
 * planted in it without violating the no-adjacent-flowers rule.
 * 
 * Example 1:
 * 
 * Input: flowerbed = [1,0,0,0,1], n = 1
 * Output: True
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: flowerbed = [1,0,0,0,1], n = 2
 * Output: False
 * 
 * 
 * 
 * Note:
 * 
 * The input array won't violate no-adjacent-flowers rule.
 * The input array size is in the range of [1, 20000].
 * n is a non-negative integer which won't exceed the input array size.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int lastPlanted = -1;
        for (int i=0; i<flowerbed.length; i++) {
            
            if (flowerbed[i] != 1 && emptyOrOutOfBounds(flowerbed, i-1, lastPlanted) 
                && emptyOrOutOfBounds(flowerbed, i+1, lastPlanted)) {
                lastPlanted = i;
                n--;
            }
        }
        
        return n <= 0;
    }
    
    private boolean emptyOrOutOfBounds(int[] flowerbed, int pos, int lastPlanted) {
        
        return pos < 0 || pos >= flowerbed.length || (lastPlanted != pos && flowerbed[pos] == 0);
    }
}
// @lc code=end
