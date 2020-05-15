/*
 * @lc app=leetcode id=419 lang=java
 *
 * [419] Battleships in a Board
 *
 * https://leetcode.com/problems/battleships-in-a-board/description/
 *
 * algorithms
 * Medium (69.02%)
 * Likes:    660
 * Dislikes: 454
 * Total Accepted:    87.4K
 * Total Submissions: 126.5K
 * Testcase Example:  '[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]'
 *
 * Given an 2D board, count how many battleships are in it. The battleships are
 * represented with 'X's, empty slots are represented with '.'s. You may assume
 * the following rules:
 * 
 * 
 * You receive a valid board, made of only battleships or empty slots.
 * Battleships can only be placed horizontally or vertically. In other words,
 * they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1
 * column), where N can be of any size.
 * At least one horizontal or vertical cell separates between two battleships -
 * there are no adjacent battleships.
 * 
 * 
 * Example:
 * X..X
 * ...X
 * ...X
 * 
 * In the above board there are 2 battleships.
 * 
 * Invalid Example:
 * ...X
 * XXXX
 * ...X
 * 
 * This is an invalid board that you will not receive - as battleships will
 * always have a cell separating between them.
 * 
 * Follow up:Could you do it in one-pass, using only O(1) extra memory and
 * without modifying the value of the board?
 */

// @lc code=start
public class Solution {
    public int countBattleships(char[][] board) {
        
        int battleshipCount = 0;
        
        for (int i=0; i<board.length; i++) {
            for (int c=0; c<board[0].length; c++) {
                if (board[i][c] == 'X' && !thereIsXLeftToPosition(i, c, board) 
                    && !thereIsXAbovePosition(i, c, board)) {
                    battleshipCount++;
                }
            }
        }
        
        return battleshipCount;
    }
    
    private boolean thereIsXAbovePosition(int f, int c, char[][] board) {
        if (f - 1 >= 0) {
            return board[f-1][c] == 'X';
        }
        
        return false;
    }
    
    private boolean thereIsXLeftToPosition(int f, int c, char[][] board) {
        if (c - 1 >= 0) {
            return board[f][c-1] == 'X';
        }
        
        return false;
    }
}
// @lc code=end
