'''

Problem Statement: Score After Flipping Matrix

Link: https://leetcode.com/problems/score-after-flipping-matrix
Tags: ['Greedy']
Difficulty: Medium

We have a two dimensional matrix grid where each value is 0 or 1.
A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score.
 



Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 
Note:

1 <= grid.length <= 20
1 <= grid[0].length <= 20
grid[i][j] is 0 or 1.




'''

