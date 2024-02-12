'''

Problem Statement: Regions Cut By Slashes

Link: https://leetcode.com/problems/regions-cut-by-slashes
Tags: ['Depth-first Search', 'Union Find', 'Graph']
Difficulty: Medium

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
Given the grid grid represented as a string array, return the number of regions.
Note that backslash characters are escaped, so a '\' is represented as '\\'.
 
Example 1:

Input: grid = [" /","/ "]
Output: 2

Example 2:

Input: grid = [" /","  "]
Output: 1

Example 3:

Input: grid = ["\\/","/\\"]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)

Example 4:

Input: grid = ["/\\","\\/"]
Output: 5
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)

Example 5:

Input: grid = ["//","/ "]
Output: 3

 
Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.



'''

