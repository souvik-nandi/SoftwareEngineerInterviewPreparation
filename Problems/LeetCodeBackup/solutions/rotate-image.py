'''
Problem Statement: Rotate Image

Link: https://leetcode.com/problems/rotate-image
Tags: ['Array']
Difficulty: Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
 
Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

 
Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def printmat(mat):
            for row in mat:
                print(row)
            print()

        n = len(matrix)
        
        for i in range(0, n // 2):
            coords = [
                (i, i), 
                (i, n - i - 1), 
                (n - i - 1, n - i - 1), 
                (n - i - 1, i)
            ]
            
            for j in range(i, n - i - 1):
                last_val = [
                    matrix[coords[0][0]][coords[0][1]], 
                    matrix[coords[1][0]][coords[1][1]], 
                    matrix[coords[2][0]][coords[2][1]], 
                    matrix[coords[3][0]][coords[3][1]]
                ]
                
                for k in range(0, 4):
                    a2, b2 = coords[(k + 1) % 4]
                    matrix[a2][b2] = last_val[k]
                
                for k in range(0, 4):
                    a, b = coords[k]
                    
                    if k == 0:
                        coords[k] = a, b + 1
                    elif k == 1:
                        coords[k] = a + 1, b
                    elif k == 2:
                        coords[k] = a, b - 1
                    else:
                        coords[k] = a - 1, b
