# 217. Contains Duplicate

## Problem Description
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1
- **Input:** `nums = [1,2,3,4,5,6,7,8,9,1]`
- **Output:** `True`

### Example 2
- **Input:** `nums = [1,2,3,4,5,6,7,8,9]`
- **Output:** `False`

## Solution
The solution utilizes a set to detect duplicates in the array.

### Algorithm

1. **Use a Set to Track Seen Elements**
   - Initialize an empty set `numsSet`.
   - Iterate through each element in the array:
     - If the element is already in the set, return `True` (indicating a duplicate).
     - Otherwise, add the element to the set.
   - If no duplicates are found by the end of the iteration, return `False`.

### Complexity
- **Time Complexity:** `O(n)`, where `n` is the number of elements in the array. Each insertion and lookup operation in a set is on average `O(1)`, so the overall complexity is linear.
- **Space Complexity:** `O(n)`, as the set can grow to hold all `n` elements in the worst case.

### Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()

        for val in nums:
            if val in numsSet:
                return True
            numsSet.add(val)

        return False
```

## Alternative Solution
Another approach is to use sorting to identify duplicates:
- **Sorting and Linear Scan:**
  1. Sort the array.
  2. Iterate through the sorted array and check if adjacent elements are the same.

### Comparison

- **Original Approach:** Utilizes a set to achieve `O(n)` time complexity and `O(n)` space complexity. This approach is efficient in terms of both time and space, especially for large arrays.

- **Alternative Approach:** Sorting the array takes `O(n log n)` time and requires `O(1)` additional space (excluding the space used by the sorting algorithm). While this approach has a better space complexity, it is slower due to the sorting step.

### Conclusion
- **Efficiency:** The original approach using a set is generally preferred for its linear time complexity, making it suitable for larger datasets.
- **Simplicity:** The sorting approach is simple but slower, making it less efficient compared to the set-based approach for detecting duplicates.

Both approaches are valid depending on the constraints and requirements of the problem.
