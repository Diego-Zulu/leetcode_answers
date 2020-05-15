/*
 * @lc app=leetcode id=681 lang=java
 *
 * [681] Next Closest Time
 *
 * https://leetcode.com/problems/next-closest-time/description/
 *
 * algorithms
 * Medium (44.54%)
 * Likes:    449
 * Dislikes: 693
 * Total Accepted:    60.7K
 * Total Submissions: 136.3K
 * Testcase Example:  '"19:34"'
 *
 * Given a time represented in the format "HH:MM", form the next closest time
 * by reusing the current digits. There is no limit on how many times a digit
 * can be reused.
 * 
 * You may assume the given input string is always valid. For example, "01:34",
 * "12:09" are all valid. "1:34", "12:9" are all invalid.
 * 
 * Example 1:
 * 
 * Input: "19:34"
 * Output: "19:39"
 * Explanation: The next closest time choosing from digits 1, 9, 3, 4, is
 * 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs
 * 23 hours and 59 minutes later.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: "23:59"
 * Output: "22:22"
 * Explanation: The next closest time choosing from digits 2, 3, 5, 9, is
 * 22:22. It may be assumed that the returned time is next day's time since it
 * is smaller than the input time numerically.
 * 
 * 
 */

// @lc code=start
class Solution {
    
    static class MilitaryTimeDigitsController {
        
        final static Character MAX_SECOND_HOUR_DIGIT = '2';
        final static Character MAX_FIRST_HOUR_DIGIT = '9';
        final static Character MAX_SECOND_MINUTE_DIGIT = '5';
        final static Character MAX_FIRST_MINUTE_DIGIT = '9';
        
        static Character getMaxCharForClockPos(int pos, Character lastDigit) {
            
            switch (pos) {
                case 0:
                    if (lastDigit > '3') {
                        return '1';
                    }
                    return MAX_SECOND_HOUR_DIGIT;
                case 1:
                    return MAX_FIRST_HOUR_DIGIT;
                case 2:
                    return ':';
                case 3:
                    return MAX_SECOND_MINUTE_DIGIT;
                case 4:
                    return MAX_FIRST_MINUTE_DIGIT;
                default:
                    return '0';
            }
        }
        
        static boolean isBiggerThanMaxForClockPos(int pos, Character digit, Character lastDigit) {

            return getMaxCharForClockPos(pos, lastDigit) < digit;
        }
    }
    
    public String nextClosestTime(String time) {
        
        LinkedList<Character> currentDigits = new LinkedList<>();
        StringBuilder result = new StringBuilder(5);
        boolean nearestHourFound = false;
        
        for (int i=0; i<time.length(); i++) {
            char c = time.charAt(i);
            if (c == ':') continue;
            currentDigits.add(c);
        }
        Collections.sort(currentDigits);
        Character lastDigit = null;
        
        for (int i=time.length() - 1; i >= 0; i--) {
            
            if (time.charAt(i) == ':') {
                result.append(':');
                continue;
            }
            Character newDigit = null;
            Iterator<Character> currentDigIt = currentDigits.iterator();
            
            while (currentDigIt.hasNext() && !nearestHourFound) {
                Character digit = currentDigIt.next();
                
                if (!MilitaryTimeDigitsController.isBiggerThanMaxForClockPos(i, digit, lastDigit) && digit > time.charAt(i)) {
                    newDigit = digit;
                    break;
                }
            }
            
            if (newDigit != null) {
                nearestHourFound = true;
            } else if (!nearestHourFound) {
                newDigit = currentDigits.peek();
            } else {
                newDigit = time.charAt(i);
            } 
            result.append(newDigit);
            lastDigit = newDigit;
        }
        
        return result.reverse().toString();
    }
}
// @lc code=end
