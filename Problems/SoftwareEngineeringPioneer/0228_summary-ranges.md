# 228. Summary Ranges

## Problem Statement

Given a sorted unique integer array `nums`, return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of `nums` should be covered by exactly one of the ranges, and there should be no integer `x` such that `x` is in one of the ranges but not in `nums`.

### Example

**Input:**
```
nums = [0,1,2,4,5,7]
```
**Output:**
```
["0->2","4->5","7"]
```

**Explanation:** The ranges are:
- [0,2] represents "0->2"
- [4,5] represents "4->5"
- [7,7] represents "7"

## Solution 1: Linear Scan Approach

### Algorithm Description

This solution iteratively scans through the `nums` array to identify ranges:

1. **Initialization**: Start with the first element as the beginning of the first range.
2. **Iterative Comparison**: Compare each number with the previous one to check if it continues the current range or starts a new one.
3. **Range Closure**: If a gap is detected (i.e., the current number is not consecutive with the previous one), close the current range and start a new one.
4. **Finalization**: After the loop, ensure the last range is added to the result.

### Key Details

- **Simple Logic**: The algorithm checks only for consecutive numbers, making it straightforward and easy to implement.
- **Edge Case Handling**: It correctly handles cases with a single element or non-consecutive elements.

### Complexity

- **Time Complexity**: O(n), where `n` is the length of the `nums` array. Each element is processed exactly once.
- **Space Complexity**: O(1), ignoring the space required for the output list.

## Solution 2: Binary Search Approach

### Algorithm Description

This solution uses a more advanced approach with binary search to identify the end of each range:

1. **Binary Search for Range Ends**: For each starting point of a range, binary search is used to find the farthest point where the range can extend.
2. **Range Identification**: After identifying the end of the range, it is added to the result.
3. **Continuation**: The process repeats for the next starting point.

### Key Details

- **Efficient for Large Gaps**: This approach can be more efficient when there are large gaps between consecutive ranges, as it skips unnecessary checks.
- **Binary Search**: Leveraging binary search helps quickly identify the boundaries of ranges.

### Complexity

- **Time Complexity**: O(n log n) in the worst case, where `n` is the length of the `nums` array. The binary search adds a logarithmic factor to the otherwise linear scan.
- **Space Complexity**: O(1), excluding the output list.

## Conclusion

Both solutions efficiently solve the "Summary Ranges" problem, with the linear scan approach being more straightforward and the binary search approach providing a potentially faster solution for certain cases. Depending on the specific characteristics of the input data, either method can be preferred. The first solution is typically faster for small arrays or arrays with many consecutive numbers, while the second might excel in cases with larger gaps.


### Code with Comments

#### Solution 1: Linear Scan Approach

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        
        ranges = []
        start = nums[0]
        last = nums[0]

        for val in nums:
            if val - last > 1:
                # Add the current range to the list
                ranges.append(f"{start}" if last == start else f"{start}->{last}")
                # Start a new range
                start = val
            last = val
        
        # Add the final range
        ranges.append(f"{start}" if last == start else f"{start}->{last}")
        return ranges
```

#### Solution 2: Binary Search Approach

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def isCorrectPos(p1, p2):
            val1 = nums[p1] if p1 < n else float('inf')
            val2 = nums[p2] if p2 < n else float('inf')
            return val2 - val1 == p2 - p1
        
        ranges = []
        n = len(nums)
        start = 0

        while start < n:
            left = start
            right = n - 1
            
            while left <= right:
                mid = (left + right) // 2
                if isCorrectPos(start, mid) and not isCorrectPos(start, mid + 1):
                    # Found the end of the range
                    ranges.append(f"{nums[start]}" if start == mid else f"{nums[start]}->{nums[mid]}")
                    start = mid + 1
                    break
                elif isCorrectPos(start, mid + 1):
                    left = mid + 1
                else:
                    right = mid - 1

        return ranges
```
