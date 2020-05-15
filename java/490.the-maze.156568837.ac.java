/*
 * @lc app=leetcode id=490 lang=java
 *
 * [490] The Maze
 *
 * https://leetcode.com/problems/the-maze/description/
 *
 * algorithms
 * Medium (50.70%)
 * Likes:    697
 * Dislikes: 74
 * Total Accepted:    59.7K
 * Total Submissions: 117.5K
 * Testcase Example:  '[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]'
 *
 * There is a ball in a maze with empty spaces and walls. The ball can go
 * through empty spaces by rolling up, down, left or right, but it won't stop
 * rolling until hitting a wall. When the ball stops, it could choose the next
 * direction.
 * 
 * Given the ball's start position, the destination and the maze, determine
 * whether the ball could stop at the destination.
 * 
 * The maze is represented by a binary 2D array. 1 means the wall and 0 means
 * the empty space. You may assume that the borders of the maze are all walls.
 * The start and destination coordinates are represented by row and column
 * indexes.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input 1: a maze represented by a 2D array
 * 
 * 0 0 1 0 0
 * 0 0 0 0 0
 * 0 0 0 1 0
 * 1 1 0 1 1
 * 0 0 0 0 0
 * 
 * Input 2: start coordinate (rowStart, colStart) = (0, 4)
 * Input 3: destination coordinate (rowDest, colDest) = (4, 4)
 * 
 * Output: true
 * 
 * Explanation: One possible way is : left -> down -> left -> down -> right ->
 * down -> right.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input 1: a maze represented by a 2D array
 * 
 * 0 0 1 0 0
 * 0 0 0 0 0
 * 0 0 0 1 0
 * 1 1 0 1 1
 * 0 0 0 0 0
 * 
 * Input 2: start coordinate (rowStart, colStart) = (0, 4)
 * Input 3: destination coordinate (rowDest, colDest) = (3, 2)
 * 
 * Output: false
 * 
 * Explanation: There is no way for the ball to stop at the destination.
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * There is only one ball and one destination in the maze.
 * Both the ball and the destination exist on an empty space, and they will not
 * be at the same position initially.
 * The given maze does not contain border (like the red rectangle in the
 * example pictures), but you could assume the border of the maze are all
 * walls.
 * The maze contains at least 2 empty spaces, and both the width and height of
 * the maze won't exceed 100.
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        
        BitSet[] isVisited = new BitSet[maze.length];
        for (int i=0; i<isVisited.length; i++) {
            isVisited[i] = new BitSet(maze[0].length);
        }
        
        return hasPathDFS(maze, start, destination, isVisited);
    }
    
    private boolean hasPathDFS(int[][] maze, int[] start, int[] destination, BitSet[] isVisited) {
        
        if (reachedEnd(start, destination)) return true;
        
        if (!visitedPos(start, isVisited)) {
            markVisited(start, isVisited);
            
            return hasPathDFS(maze, leftMove(maze, start), destination, isVisited) 
                || hasPathDFS(maze, rightMove(maze, start), destination, isVisited) 
                || hasPathDFS(maze, bottomMove(maze, start), destination, isVisited) 
                || hasPathDFS(maze, topMove(maze, start), destination, isVisited);
        }
        return false;
    }
    
    private void markVisited(int[] pos, BitSet[] isVisited) {
        isVisited[pos[0]].set(pos[1]);
    }
    
    private int[] leftMove(int[][] maze, int[] pos) {
        int i = pos[0];
        int j = pos[1];
        while (i >= 0 && maze[i][j] != 1) i--;
        return new int [] {i + 1, j};
    }
    
    private int[] rightMove(int[][] maze, int[] pos) {
        int i = pos[0];
        int j = pos[1];
        while (i < maze.length && maze[i][j] != 1) i++;
        return new int [] {i - 1, j};
    }
    
    private int[] topMove(int[][] maze, int[] pos) {
        int i = pos[0];
        int j = pos[1];
        while (j >= 0 && maze[i][j] != 1) j--;
        return new int [] {i, j + 1};
    }
    
    private int[] bottomMove(int[][] maze, int[] pos) {
        int i = pos[0];
        int j = pos[1];
        while (j < maze[0].length && maze[i][j] != 1) j++;
        return new int [] {i, j - 1};
    }
    
    private boolean reachedEnd(int[] pos, int[] end) {
        
        return pos[0] == end[0] && pos[1] == end[1];
    }
    
    private boolean visitedPos(int[] pos, BitSet[] isVisited) {
        
        return isVisited[pos[0]].get(pos[1]);
    }
}
// @lc code=end
