/*
 * @lc app=leetcode id=346 lang=java
 *
 * [346] Moving Average from Data Stream
 *
 * https://leetcode.com/problems/moving-average-from-data-stream/description/
 *
 * algorithms
 * Easy (69.78%)
 * Likes:    513
 * Dislikes: 54
 * Total Accepted:    113.9K
 * Total Submissions: 163.2K
 * Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
 *
 * Given a stream of integers and a window size, calculate the moving average
 * of all integers in the sliding window.
 * 
 * Example:
 * 
 * 
 * MovingAverage m = new MovingAverage(3);
 * m.next(1) = 1
 * m.next(10) = (1 + 10) / 2
 * m.next(3) = (1 + 10 + 3) / 3
 * m.next(5) = (10 + 3 + 5) / 3
 * 
 * 
 * 
 * 
 */

// @lc code=start
class MovingAverage {
    Queue<Integer> stream;
    int size;
    double sum;
        
    /** Initialize your data structure here. */
    public MovingAverage(int s) {
        stream = new LinkedList<>();
        size = s;
        sum = 0;
    }
    
    public double next(int val) {

        if (stream.size() == size) {
            sum -= stream.remove();
        }
        stream.offer(val);
        sum += val;
        
        return sum / stream.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
// @lc code=end
