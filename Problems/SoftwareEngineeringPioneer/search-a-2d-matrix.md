# 74. Search a 2D Matrix

## Problem Description
You are given an `m x n` integer matrix `matrix` with the following properties:
- Each row is sorted in ascending order.
- Each column is also sorted in ascending order.

Given an integer `target`, write a function to determine if `target` exists in the matrix.

### Example 1
- **Input:** `matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 5`
- **Output:** `True`

### Example 2
- **Input:** `matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 20`
- **Output:** `False`

## Solution
The solution uses two binary search operations to efficiently locate the target in the matrix.

### Algorithm

1. **Binary Search to Find the Row**
   - Perform binary search on the rows to determine which row might contain the target. 
   - Each row is compared based on its first element and the first element of the next row to decide if the target is in the current row.

2. **Binary Search within the Found Row**
   - Once the potential row is identified, perform a binary search within that row to find the exact column containing the target.

### Complexity
- **Time Complexity:** `O(log m + log n)`, where `m` is the number of rows and `n` is the number of columns. Binary search on rows takes `O(log m)`, and binary search within the row takes `O(log n)`.
- **Space Complexity:** `O(1)`, as no additional space is used apart from the input variables.

### Code

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows (m) and columns (n) in the matrix
        m = len(matrix)
        n = len(matrix[0])
        targetRow = -1

        # Binary Search to Find the Row that could contain the Target
        left = 0
        right = m - 1

        while left <= right:
            mid = (left + right) // 2
            midVal = matrix[mid][0]  # First element of the mid row
            rightVal = matrix[mid + 1][0] if mid < m - 1 else float('inf')  # First element of the next row

            # Check if the target is in the current row
            if midVal <= target < rightVal:
                targetRow = mid
                break
            elif midVal > target:
                right = mid - 1  # Target is in an earlier row
            else:
                left = mid + 1  # Target is in a later row

        # If no valid row was found, return False
        if targetRow == -1:
            return False

        # Binary Search within the Found Row to Find the Exact Column
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            midVal = matrix[targetRow][mid]  # Element at the mid column of the target row

            if midVal == target:
                return True  # Target found
            elif midVal > target:
                right = mid - 1  # Target is in an earlier column
            else:
                left = mid + 1  # Target is in a later column
        
        # If target is not found in the row, return False
        return False
```

## Alternative Solution
Another approach is to use a more straightforward but less efficient solution:
- **Linear Scan:** Start from the top-right corner of the matrix and move left or down based on comparisons with the target.

### Comparison
- **Original Approach:** Uses binary search twice, once to find the row and once within the row, providing a time complexity of `O(log m + log n)`. This is more efficient for larger matrices with sorted properties.
- **Alternative Approach:** Involves a single traversal starting from the top-right, which has a time complexity of `O(m + n)`. While this method is simpler and avoids additional logarithmic factors, it is generally less efficient than the original approach for large matrices.

Both approaches are valid, and the choice depends on specific requirements for efficiency and simplicity.
