# 73. Set Matrix Zeroes

## Problem Description
Given an `m x n` integer matrix `matrix`, if an element in the matrix is `0`, set its entire row and column to `0`. Do this in-place.

### Example
- **Input:**
  ```python
  matrix = [
      [1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]
  ]
  ```
- **Output:**
  ```python
  [
      [1, 0, 1],
      [0, 0, 0],
      [1, 0, 1]
  ]
  ```

## Solution 1: Using Sets to Track Rows and Columns

### Algorithm

1. **Identify Zero Rows and Columns**
   - Traverse the matrix to find which rows and columns contain zeros. Store these in sets.

2. **Set Rows and Columns to Zero**
   - Iterate through the matrix again. If the current row or column is in the zero-sets, set the corresponding cell to zero.

### Code

```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowsWithZeros = set()
        colsWithZeros = set()

        m = len(matrix)
        n = len(matrix[0])

        # First pass: Identify rows and columns that need to be zeroed
        for rowIdx in range(m):
            for colIdx in range(n):
                if matrix[rowIdx][colIdx] == 0:
                    rowsWithZeros.add(rowIdx)
                    colsWithZeros.add(colIdx)

        # Second pass: Set the identified rows and columns to zero
        for rowIdx in range(m):
            for colIdx in range(n):
                if rowIdx in rowsWithZeros or colIdx in colsWithZeros:
                    matrix[rowIdx][colIdx] = 0
```

### Complexity
- **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns. Each cell is checked twice, once for marking and once for setting zeroes.
- **Space Complexity:** `O(m + n)`, for storing rows and columns indices that need to be zeroed.

## Solution 2: Using Matrix as Markers

### Algorithm

1. **Check First Row and Column**
   - Check if the first row and column need to be zeroed.

2. **Mark Zeroes in First Row and Column**
   - Traverse the matrix and use the first row and column to mark which rows and columns should be zeroed.

3. **Set Zeroes Based on Markers**
   - Use the markers in the first row and column to set the appropriate cells to zero.

4. **Handle First Row and Column Separately**
   - Zero out the first row and column if they initially contained zeroes.

### Code

```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        # Check if the first row and first column need to be zeroed
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # Mark the rows and columns that need to be zeroed
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
```

### Complexity
- **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns. The matrix is traversed a few times.
- **Space Complexity:** `O(1)`, as no additional space is used for storing rows and columns indices.

## Comparison

### Using Sets to Track Rows and Columns
- **Pros:**
  - **Straightforward:** Easy to understand and implement.
  - **Explicit Tracking:** Clearly tracks which rows and columns need to be zeroed.
- **Cons:**
  - **Extra Space:** Requires additional space to store the indices of rows and columns.

### Using Matrix as Markers
- **Pros:**
  - **Space Efficient:** Does not require additional space for tracking rows and columns.
  - **In-place Modification:** Modifies the matrix in-place without using extra space.
- **Cons:**
  - **Complexity:** Slightly more complex to understand due to the need for multiple passes and handling special cases for the first row and column.

### Conclusion
- **Solution 1 (Using Sets):** Suitable for cases where space complexity is not a major concern. Provides a clear and direct method for solving the problem.
- **Solution 2 (Using Matrix as Markers):** Preferred for its space efficiency and in-place modification. Ideal when minimizing space usage is crucial.

Both solutions effectively solve the problem, and the choice depends on the trade-off between space and complexity. 
