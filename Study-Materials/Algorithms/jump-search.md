# Jump Search

## Problem Description

The `jumpSearch` function is used to find the index of a target value in a sorted list of integers. Jump search is an algorithm designed to jump ahead by fixed steps to reduce the search space quickly, and then perform a linear search within the identified block.

## Problem Example

Given a sorted list of integers and a target value, the function returns the index of the target if it exists in the list. If the target is not found, the function returns `-1`.

### Example:
```python
nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
# Output: 3 (since nums[3] == 7)

target = 8
# Output: -1 (since 8 is not in the list)
```

## Possible Solutions - One Phrase

1. **Jump Search**: Jump ahead by fixed steps and then linearly search within the identified block.

## Solution Explanation

### 1. Jump Search

The `jumpSearch` function implements the jump search algorithm, which combines jumping and linear search to efficiently find the target value in a sorted list.

### Algorithm Description

1. **Jump Step Size**:
   - Calculate the optimal jump step size, typically the square root of the size of the list, i.e., `step = int(sqrt(n))`, where `n` is the size of the list.

2. **Jump Phase**:
   - Start from the beginning of the list and jump ahead by the step size until the value at the current position is greater than or equal to the target or until the end of the list is reached.

3. **Linear Search Phase**:
   - Once the block containing the target is identified, perform a linear search within that block.

4. **Termination**:
   - Return the index of the target if found, otherwise return `-1`.

### Code:
```python
import math
from typing import List

def jumpSearch(nums: List[int], target: int) -> int:
    n = len(nums)
    step = int(math.sqrt(n))
    prev = 0

    # Jump phase
    while nums[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search phase
    for idx in range(prev, min(step, n)):
        if nums[idx] == target:
            return idx

    return -1
```

### Time and Space Complexity

- **Time Complexity**: 
  - The time complexity of jump search is `O(√n + k)`, where `k` is the number of elements checked in the linear search phase. In the worst case, this is approximately `O(√n)`.

- **Space Complexity**: 
  - The space complexity is `O(1)` because no additional space is used that scales with the input size.

### Potential Pitfalls

1. **Step Size**: 
   - Choosing an appropriate step size is crucial. A step size too large can result in missing the target, while a step size too small can reduce the efficiency of the jump phase.

2. **Sorted Data**: 
   - Jump search assumes the data is sorted. If the data is not sorted, the algorithm may not work correctly.

## Comparison with Other Search Algorithms

### Linear Search Overview

Linear search involves iterating through each element until the target is found or the end of the list is reached.

### Code Example:
```python
def linearSearch(nums: List[int], target: int) -> int:
    for idx, value in enumerate(nums):
        if value == target:
            return idx
    return -1
```

### Binary Search Overview

Binary search repeatedly divides the search interval in half to locate the target in a sorted list.

### Code Example:
```python
def binarySearch(nums: List[int], target: int) -> int:
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
   - **Jump Search**: Offers `O(√n)` complexity, which is beneficial for large datasets when the data is sorted and a good step size is chosen.
   - **Linear Search**: Has a time complexity of `O(n)`, making it inefficient for large datasets but simple to implement.
   - **Binary Search**: Has a time complexity of `O(log n)` but requires sorted data and is not suitable for unbounded or very large datasets.

2. **Use Case**:
   - **Jump Search**: Useful for large sorted arrays where a compromise between binary search and linear search is needed.
   - **Linear Search**: Best for small or unsorted data where simplicity is desired.
   - **Binary Search**: Preferred for large, sorted arrays where the target is expected to be somewhere in the middle.

3. **Space Complexity**:
   - **Jump Search**: `O(1)`
   - **Linear Search**: `O(1)`
   - **Binary Search**: Typically `O(1)` for iterative implementations but `O(log n)` for recursive implementations due to call stack space.

### Conclusion on When to Use Each

- Use **jump search** when working with large sorted arrays where an optimal step size can be chosen, and where binary search might be overkill.
- Use **linear search** for small or unsorted data where its simplicity outweighs its inefficiency.
- Use **binary search** for large, sorted arrays when optimal `O(log n)` performance is needed.
