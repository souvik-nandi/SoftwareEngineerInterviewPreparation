# 1. Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Example 1
- **Input:** `nums = [2, 7, 11, 15], target = 9`
- **Output:** `[0, 1]`  
  (Because `nums[0] + nums[1] = 2 + 7 = 9`)

### Example 2
- **Input:** `nums = [3, 2, 4], target = 6`
- **Output:** `[1, 2]`  
  (Because `nums[1] + nums[2] = 2 + 4 = 6`)

## Solution
The solution uses a hash map (dictionary) to store the indices of the numbers while iterating through the array. This allows for constant-time lookups to check if the complementary number needed to reach the target exists.

### Algorithm

1. **Initialize a Dictionary**
   - Create an empty dictionary `numsMap` to store the number as the key and its index as the value.

2. **Iterate Through the Array**
   - For each number in the array, calculate the `remaining` value needed to reach the target.
   - Check if the `remaining` value is already in the dictionary:
     - If it is, return the indices of the `remaining` value and the current number.
     - If it is not, store the current number and its index in the dictionary.

3. **Return the Indices**
   - If no solution is found by the end of the iteration, return `[-1, -1]` (although the problem guarantees a solution exists).

### Complexity
- **Time Complexity:** `O(n)`, where `n` is the number of elements in the array. Each number is processed once, and dictionary operations are average `O(1)`.
- **Space Complexity:** `O(n)`, due to the space required to store up to `n` elements in the dictionary.

### Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for idx, item in enumerate(nums):
            remaining = target - item

            if remaining in numsMap:
                return [numsMap[remaining], idx]
            numsMap[item] = idx
        
        return [-1, -1]
```

## Alternative Solution
Another approach is to use a brute-force method:
- **Brute-Force Approach:** 
  1. Use two nested loops to check all pairs of numbers to see if they add up to the target.

### Comparison

- **Original Approach:** Utilizes a dictionary to achieve `O(n)` time complexity. This method is efficient as it only requires a single pass through the array and constant-time lookups.

- **Alternative Approach:** The brute-force method has a time complexity of `O(n^2)`, where `n` is the number of elements in the array. This method involves checking every possible pair of numbers and is less efficient for larger arrays.

### Conclusion
- **Efficiency:** The original approach using a dictionary is highly efficient and preferred for its linear time complexity and constant-time lookups.
- **Simplicity:** The brute-force approach is simpler but less efficient, making it suitable only for small arrays or scenarios where performance is not a concern.

Both approaches are valid, but the dictionary-based method is generally preferred for its efficiency in solving the problem.
