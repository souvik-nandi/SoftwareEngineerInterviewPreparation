## 153. Find Minimum in Rotated Sorted Array

The problem requires finding the minimum element in a rotated sorted array. A rotated array is a sorted array that has been rotated around an unknown pivot, so the array might be split into two subarrays that are sorted. The goal is to identify the minimum element in the array.

## Problem Examples

**Example 1:**

- **Input:** `nums = [3, 4, 5, 1, 2]`
- **Output:** `1`
- **Explanation:** The original sorted array is `[1, 2, 3, 4, 5]`. After rotating around the pivot, the minimum element is `1`.

**Example 2:**

- **Input:** `nums = [4, 5, 6, 7, 0, 1, 2]`
- **Output:** `0`
- **Explanation:** The original sorted array is `[0, 1, 2, 4, 5, 6, 7]`. The minimum element is `0`.

**Example 3:**

- **Input:** `nums = [11, 13, 15, 17]`
- **Output:** `11`
- **Explanation:** The array is not rotated. The minimum element is the first element, `11`.

## Possible Solutions

1. **Binary Search-based approach:**

## Solution 1: Binary Search-based Approach

### Code:

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge cases:
        # 1. If the list is empty, return -1 (error code).
        if n == 0:
            return -1
        
        # 2. If the list has only one element or is not rotated (sorted in ascending order),
        #    return the first element as the minimum.
        if n == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the middle element is the minimum:
            # If the current element is less than both its neighbors (or at boundaries), it's the minimum.
            if (mid == 0 or nums[mid - 1] > nums[mid]) and (mid == n - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            
            # Trick: Determine the sorted half and decide which half to search next:
            # 1. If the middle element is greater than the last element, it means the minimum is in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 2. Otherwise, the minimum is in the left half.
                right = mid - 1

        # Shouldn't reach here if the input is valid, but return -1 as a fallback.
        return -1
```

### Algorithm Description:

The solution utilizes a binary search approach to minimize the number of comparisons and efficiently find the minimum element. The key insight is that the minimum element will always be in the unsorted part of the rotated array. By continuously narrowing the search space based on the middle element's comparison with the rightmost element, the algorithm converges on the minimum.

### Complexity Analysis:

- **Time Complexity:** `O(log n)` - The binary search approach cuts down the search space by half each time, leading to a logarithmic time complexity.
- **Space Complexity:** `O(1)` - The solution only requires a constant amount of space, as it uses a few pointers and variables.

### Potential Pitfalls:

- Edge cases where the array is not rotated, contains only one element, or is empty need to be handled carefully.
- The algorithm assumes the input is valid; otherwise, a fallback return of `-1` is used.

## Comparison with Other Solutions

### Brute Force Solution:

**Algorithm Description:** The simplest approach would be to iterate through the entire array and find the minimum element by comparing each element with the others.

**Complexity Analysis:**
- **Time Complexity:** `O(n)` - The entire array is traversed, making it less efficient.
- **Space Complexity:** `O(1)` - No additional space is required apart from a few variables.

**Drawbacks:** The brute force method is slower for large arrays, as it does not take advantage of the array's sorted and rotated properties.

**Conclusion:** 

The binary search-based approach is significantly better than the brute-force method, as it takes advantage of the array's properties and achieves logarithmic time complexity. Therefore, it is the preferred solution when dealing with this problem.
