/*
 * @lc app=leetcode id=121 lang=java
 *
 * [121] Best Time to Buy and Sell Stock
 *
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
 *
 * algorithms
 * Easy (49.94%)
 * Likes:    4596
 * Dislikes: 205
 * Total Accepted:    810.4K
 * Total Submissions: 1.6M
 * Testcase Example:  '[7,1,5,3,6,4]'
 *
 * Say you have an array for which the i^th element is the price of a given
 * stock on day i.
 * 
 * If you were only permitted to complete at most one transaction (i.e., buy
 * one and sell one share of the stock), design an algorithm to find the
 * maximum profit.
 * 
 * Note that you cannot sell a stock before you buy one.
 * 
 * Example 1:
 * 
 * 
 * Input: [7,1,5,3,6,4]
 * Output: 5
 * Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit
 * = 6-1 = 5.
 * Not 7-1 = 6, as selling price needs to be larger than buying price.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [7,6,4,3,1]
 * Output: 0
 * Explanation: In this case, no transaction is done, i.e. max profit = 0.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int maxProfit(int[] prices) {
        //int[] result = {Integer.MIN_VALUE};
        //calculateMaxProfit(prices, result, 0, prices.length, 0, 0);
        //return result[0];
        
        int min = 0;
        int max = 0;
        int profit = 0;
        
        for (int i=0; i<prices.length; i++) {
            if (prices[min] > prices[i]) {
                min = i;
                if (min > max) max = min;
            }
            
            if (prices[max] < prices[i]) {
                max = i;
            }
            
            if (prices[max] - prices[min] > profit) profit = prices[max] - prices[min];
        }
        
        return profit;
    }
    
    /*private void calculateMaxProfit(int[] prices, int[] result, int day, int maximumDay, int actualProfit, int amountOfShares) {
        
        if (day < maximumDay) {
            
                calculateMaxProfit(prices, result, day+1, maximumDay, actualProfit, amountOfShares);
   
                calculateMaxProfit(prices, result, day+1, maximumDay, actualProfit - prices[day], amountOfShares + 1);
                
                if (amountOfShares > 0)
                calculateMaxProfit(prices, result, day+1, maximumDay, actualProfit + prices[day], amountOfShares - 1);
            
        } else {
            if (result[0] < actualProfit) {
                result[0] = actualProfit;
            }
        }
    }*/
}
// @lc code=end
