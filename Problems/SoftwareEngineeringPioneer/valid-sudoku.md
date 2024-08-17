# 36. Valid Sudoku

## Problem Description
Determine if a `9x9` Sudoku board is valid. Only the following rules need to be checked:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Empty cells are represented by the `'.'` character.

### Example
- **Input:**
  ```python
  board = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".",".",".",".",".","6"],
      [".",".",".","4",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","8"],
      [".",".",".",".","8",".",".","7","9"]
  ]
  ```
- **Output:**
  ```python
  True
  ```

## Solution 1: Using Sets for Rows, Columns, and Sub-Boxes

### Algorithm

1. **Initialize Sets**
   - Create three lists of sets: one for rows, one for columns, and one for `3x3` sub-boxes.

2. **Iterate Through the Board**
   - For each cell in the board, skip empty cells.
   - Check if the number has already been seen in the current row, column, or sub-box. If yes, the board is invalid.
   - If not, add the number to the corresponding sets.

3. **Return the Result**
   - If no duplicates are found, the board is valid.

### Code

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track seen numbers in rows, columns, and sub-boxes
        rowVals = [set() for _ in range(9)]
        colVals = [set() for _ in range(9)]
        gridVals = [set() for _ in range(9)]
        
        # Iterate through each cell in the board
        for rowIdx in range(9):
            for colIdx in range(9):
                if board[rowIdx][colIdx] == ".":
                    continue

                # Convert cell value to integer
                val = int(board[rowIdx][colIdx])
                # Calculate the index for the 3x3 sub-box
                gridIdx = (rowIdx // 3) * 3 + (colIdx // 3)

                # Check for duplicates in the row, column, or sub-box
                if val in rowVals[rowIdx] or val in colVals[colIdx] or val in gridVals[gridIdx]:
                    return False
                
                # Add the value to the corresponding sets
                rowVals[rowIdx].add(val)
                colVals[colIdx].add(val)
                gridVals[gridIdx].add(val)
                
        return True
```

### Complexity
- **Time Complexity:** `O(1)`, since the board size is fixed at `9x9`, and each cell is processed a constant number of times.
- **Space Complexity:** `O(1)`, since the space used for sets is constant and does not depend on the input size.

## Alternative Solution: Using Single Set with Composite Key

### Algorithm

1. **Use a Single Set**
   - Create a single set to track seen values using composite keys.

2. **Composite Key Construction**
   - Construct a key for each cell combining row index, column index, and sub-box index.

3. **Check for Duplicates**
   - For each cell, check if the composite key is already in the set. If yes, the board is invalid.
   - Otherwise, add the composite key to the set.

### Code

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        # Iterate through each cell in the board
        for rowIdx in range(9):
            for colIdx in range(9):
                if board[rowIdx][colIdx] == ".":
                    continue

                # Convert cell value to integer
                val = board[rowIdx][colIdx]

                # Construct composite keys for row, column, and sub-box
                rowKey = f"row_{rowIdx}_{val}"
                colKey = f"col_{colIdx}_{val}"
                gridKey = f"grid_{rowIdx // 3}_{colIdx // 3}_{val}"

                # Check if any key is already in the set
                if rowKey in seen or colKey in seen or gridKey in seen:
                    return False

                # Add keys to the set
                seen.add(rowKey)
                seen.add(colKey)
                seen.add(gridKey)
        
        return True
```

### Complexity
- **Time Complexity:** `O(1)`, similar to the previous solution, due to the fixed size of the board.
- **Space Complexity:** `O(1)`, space usage is constant with respect to the input size.

## Comparison

### Using Sets for Rows, Columns, and Sub-Boxes
- **Pros:**
  - **Simple and Intuitive:** Directly maps to the problem constraints.
  - **Easy to Implement:** Clear separation of concerns for rows, columns, and sub-boxes.
- **Cons:**
  - **Multiple Data Structures:** Requires maintaining three separate sets.

### Using Single Set with Composite Key
- **Pros:**
  - **Compact Solution:** Uses a single set to track all constraints.
  - **Less Overhead:** Simplifies the data structures used.
- **Cons:**
  - **Composite Key Management:** Requires constructing and managing composite keys.

### Conclusion
- **Solution 1 (Using Sets):** Preferred for its clarity and straightforward approach. Ideal for those who prefer separate tracking for rows, columns, and sub-boxes.
- **Solution 2 (Using Single Set with Composite Key):** More compact and slightly more elegant, though it involves managing composite keys.

Both solutions are efficient and solve the problem correctly. The choice depends on personal preference and clarity of code.
