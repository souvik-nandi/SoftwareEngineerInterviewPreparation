## 162. Find Peak Element

The problem requires finding a peak element in an array. A peak element is an element that is greater than its neighbors. If the array contains multiple peaks, the algorithm should return the index of any one of the peaks. The array may contain negative, positive, or zero values, and the peaks do not need to be unique.

## Problem Examples

**Example 1:**

- **Input:** `nums = [1, 2, 3, 1]`
- **Output:** `2`
- **Explanation:** The peak element is `3` at index `2`.

**Example 2:**

- **Input:** `nums = [1, 2, 1, 3, 5, 6, 4]`
- **Output:** `5`
- **Explanation:** The peak element is `6` at index `5`. The algorithm could also return `1` as `2` is also a peak.

## Possible Solutions

### Solution 1: Binary Search-based Approach

This approach leverages binary search to efficiently find a peak element in the array. By comparing the middle element with its neighbors, the algorithm decides which half of the array to search next. The insight here is that if the middle element is not a peak, then a peak must exist in the direction of the larger neighbor, ensuring that the search space is reduced by half each iteration.

#### Code:

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]
            leftVal = nums[mid-1] if mid > 0 else float('-inf')
            rightVal = nums[mid+1] if mid < n-1 else float('-inf')

            # Check if mid is a peak
            if leftVal < midVal and rightVal < midVal:
                return mid
            # Move to the left half if left neighbor is greater
            elif leftVal > midVal:
                right = mid - 1
            # Move to the right half otherwise
            else:
                left = mid + 1

        return -1  # Fallback in case of an invalid input
```

### Algorithm Description:

1. **Initialization:** 
   - The algorithm initializes two pointers, `left` and `right`, to the start and end of the array, respectively.

2. **Binary Search Loop:**
   - The `mid` index is calculated by taking the average of `left` and `right`.
   - The `midVal` is compared with its neighbors (`leftVal` and `rightVal`).
   - If `midVal` is greater than both neighbors, it is the peak, and the index is returned.
   - If `leftVal` is greater than `midVal`, the peak must be on the left side, so `right` is moved to `mid - 1`.
   - Otherwise, the peak must be on the right side, so `left` is moved to `mid + 1`.

3. **Edge Handling:**
   - Special cases are handled using boundary checks, where if `mid` is the first or last element, the corresponding neighbor is considered as `-inf`.

### Complexity Analysis:

- **Time Complexity:** `O(log n)` - The binary search approach reduces the search space by half each time, leading to a logarithmic time complexity.
- **Space Complexity:** `O(1)` - The solution uses a constant amount of additional space, requiring only a few pointers.

### Potential Pitfalls:

- This solution assumes that the input array is valid. If the array is empty or contains only one element, it must be handled separately.
- The algorithm guarantees finding a peak but doesn't guarantee finding all peaks.

### Alternative Solution: Linear Scan

**Algorithm Description:**
- A simple approach would be to perform a linear scan of the array, comparing each element with its neighbors to identify a peak.

**Complexity Analysis:**
- **Time Complexity:** `O(n)` - The entire array is traversed, leading to linear time complexity.
- **Space Complexity:** `O(1)` - Requires constant space for a few variables.

**Drawbacks:**
- While this method is straightforward, it is less efficient than the binary search approach, especially for large arrays.

### Conclusion

The binary search-based approach is significantly better than the linear scan method because it leverages the properties of the peak finding problem to achieve logarithmic time complexity. The linear scan method, although simpler, is less efficient and should be used only in contexts where simplicity is prioritized over performance.
