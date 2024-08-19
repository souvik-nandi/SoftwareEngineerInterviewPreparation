# Exponential Search

## Problem Description

The goal of the `exponentialSearch` function is to find the index of a given target value in a sorted list of integers. The function leverages the exponential search algorithm, which is efficient for finding an element in a sorted array, especially when the element is closer to the beginning of the array.

## Problem Example

Given a sorted list of integers and a target value, the function returns the index of the target if it exists in the list. If the target is not found, the function returns `-1`.

### Example:
```python
nums = [1, 2, 3, 5, 7, 8, 10, 15]
target = 5
# Output: 3 (since nums[3] == 5)

target = 6
# Output: -1 (since 6 is not in the list)
```

## Possible Solutions - One Phrase

1. **Exponential Search**: Start with a small range and exponentially increase it to find the target or narrow the search space.

## Solution Explanation

### 1. Exponential Search

The `exponentialSearch` function is designed to efficiently search for a target value in a sorted list by using the exponential search technique. 

### Algorithm Description

1. **Initial Step**: 
   - Begin by checking if the target is at the `baseIdx`. If it is, return `baseIdx`.
   
2. **Exponential Growth**:
   - Start with an index `idx` initialized to 1.
   - Double `idx` until the `pos` index (which is `baseIdx + idx`) exceeds the `lastIdx` or the value at `pos` is greater than the target.

3. **Narrowing the Range**:
   - Once the loop breaks, narrow down the search range by defining a new base index (`newBaseIdx`) and a new last index (`newLastIdx`).
   - Recursively search within this narrowed range.

4. **Termination**:
   - If the search range cannot be reduced further (`newBaseIdx == baseIdx` and `newLastIdx == lastIdx`), return `-1` to indicate the target is not found.

### Code:
```python
def exponentialSearch(baseIdx, lastIdx, nums, target):
    idx = 1
    pos = baseIdx + idx

    if target == nums[baseIdx]:
        return baseIdx
    
    # Exponential search step
    while pos <= lastIdx and nums[pos] <= target:
        idx *= 2
        pos = baseIdx + idx

    # Recursive call within the narrowed range
    newBaseIdx = baseIdx + (idx // 2)
    newLastIdx = min(pos, lastIdx)

    if newBaseIdx == baseIdx and newLastIdx == lastIdx:
        return -1
    
    return exponentialSearch(newBaseIdx, newLastIdx, nums, target)
```

### Time and Space Complexity

- **Time Complexity**: 
  - The time complexity of the exponential search algorithm is `O(log i)`, where `i` is the position of the target in the array. In the worst case, the complexity is `O(log n)`.

- **Space Complexity**: 
  - The space complexity is `O(log n)` due to the recursive stack space.

### Potential Pitfalls

1. **Out-of-Bounds Access**: 
   - Ensure the index `pos` does not exceed the `lastIdx` during the exponential growth phase to prevent out-of-bounds errors.
   
2. **Infinite Recursion**: 
   - Ensure the base index and last index are updated correctly to prevent infinite recursion. The condition `newBaseIdx == baseIdx and newLastIdx == lastIdx` is critical for termination.

## Comparison with Binary Search

### Binary Search Overview

Binary search is another efficient algorithm used to find the position of a target value in a sorted array. It works by repeatedly dividing the search interval in half and comparing the target value to the middle element of the current search range.

### Code Example:
```python
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

### Comparison

1. **Performance**:
   - **Binary Search**: Always has a time complexity of `O(log n)` regardless of the position of the target in the array.
   - **Exponential Search**: Can outperform binary search when the target is closer to the beginning of the array, as its time complexity is `O(log i)`, where `i` is the index of the target.

2. **Use Case**:
   - **Binary Search**: Preferred for uniformly distributed data where the position of the target is unknown and could be anywhere in the array.
   - **Exponential Search**: Ideal when there is a higher likelihood that the target is near the start of the array, or when dealing with unbounded or very large data sets.

3. **Space Complexity**:
   - **Binary Search**: Typically has a space complexity of `O(1)` when implemented iteratively.
   - **Exponential Search**: Requires `O(log n)` space due to recursion.

4. **Implementation**:
   - **Binary Search**: Easier to implement and understand, making it a more common choice.
   - **Exponential Search**: Slightly more complex, but advantageous in specific scenarios where the target is likely near the start.

### Conclusion on When to Use Each

- Use **binary search** when you need a consistent `O(log n)` performance across any target position within the array.
- Use **exponential search** when you suspect the target may be closer to the start of the array, potentially reducing the search time to `O(log i)` where `i` is small.
