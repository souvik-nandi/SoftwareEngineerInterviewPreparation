## 704. Binary Search

Given a sorted array of integers `nums` and a target value `target`, write a function to search for `target` in `nums`. If `target` exists, return its index. Otherwise, return `-1`.

You must implement an algorithm with `O(log n)` runtime complexity.

### Problem Examples

#### Example 1:
- **Input:** `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`
- **Output:** `4`
- **Explanation:** `9` exists in `nums` and its index is `4`.

#### Example 2:
- **Input:** `nums = [-1, 0, 3, 5, 9, 12]`, `target = 2`
- **Output:** `-1`
- **Explanation:** `2` does not exist in `nums`, so return `-1`.

#### Example 3:
- **Input:** `nums = [2, 5]`, `target = 5`
- **Output:** `1`
- **Explanation:** `5` exists in `nums` and its index is `1`.

### Possible Solutions

1. **Iterative Binary Search**

### Solution 1: Iterative Binary Search

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
```

#### Algorithm Description

1. **Initialize Pointers**:
   - Set two pointers, `left` at the beginning of the array (index `0`) and `right` at the end of the array (index `len(nums) - 1`).

2. **Binary Search Loop**:
   - Calculate the middle index `mid` as the integer division of `(left + right) // 2`.
   - Compare the value at `nums[mid]` with the target:
     - If `nums[mid]` is equal to the target, return `mid` as the index where the target is found.
     - If `nums[mid]` is less than the target, move the `left` pointer to `mid + 1`, searching the right half of the array.
     - If `nums[mid]` is greater than the target, move the `right` pointer to `mid - 1`, searching the left half of the array.
   - Continue this process until the `left` pointer exceeds the `right` pointer, meaning the target is not in the array.

3. **Return -1 if Not Found**:
   - If the loop completes without finding the target, return `-1`, indicating the target is not in the array.

#### Complexity Analysis

- **Time Complexity**: `O(log n)`
  - The algorithm halves the search space with each iteration, making it logarithmic in complexity.
  
- **Space Complexity**: `O(1)`
  - The algorithm only uses a constant amount of extra space, regardless of the size of the input array.

#### Potential Pitfalls

1. **Incorrect Mid Calculation**:
   - Ensure that the mid index is correctly calculated as the integer division of `(left + right) // 2` to avoid errors in pointer updates.

2. **Off-by-One Errors**:
   - Care must be taken to properly update the `left` and `right` pointers, ensuring they narrow the search space correctly without skipping potential target positions.

3. **Handling Edge Cases**:
   - Consider edge cases where the array might be empty, contain a single element, or where the target is at the boundaries of the array.

### Conclusion

The iterative binary search is the optimal solution for this problem due to its logarithmic time complexity, which meets the requirement of `O(log n)`. This approach is efficient for searching in a sorted array and handles various edge cases effectively.
