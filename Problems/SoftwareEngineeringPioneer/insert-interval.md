# 57. Insert Interval

## Problem Statement

You are given an array of non-overlapping intervals sorted by their start time. You are also given a new interval to insert into the array. The task is to insert the new interval into the correct position, merging if necessary, and return the resulting array of intervals.

### Example

**Input:**
```
intervals = [[1,3],[6,9]]
newInterval = [2,5]
```
**Output:**
```
[[1,5],[6,9]]
```

**Explanation:** The new interval `[2,5]` overlaps with `[1,3]`, so they are merged into `[1,5]`.

## Solution: Optimized Iterative Approach

### Algorithm Description

The optimized solution iterates through the given intervals in a single pass and handles three main scenarios:

1. **Non-overlapping before**: Intervals that end before the new interval starts are added directly to the result list.
2. **Overlapping**: Intervals that overlap with the new interval are merged into a single interval by updating the start and end to the minimum start and maximum end.
3. **Non-overlapping after**: Intervals that start after the new interval ends are added directly to the result list after the merged interval.

### Key Tricks

- **Early Merge**: The merging of overlapping intervals is done within a single loop, which simplifies the logic and avoids unnecessary checks.
- **Three Phases**: The algorithm is divided into three distinct phases, making it both clear and efficient.

### Complexity

- **Time Complexity**: O(n), where `n` is the number of intervals. The algorithm processes each interval exactly once.
- **Space Complexity**: O(1) (excluding the output list). The space is used only for the result list.

## Conclusion

This optimized solution efficiently inserts and merges intervals in a single pass, making it both time and space-efficient. The clear separation of logic into three phases ensures that the code is easy to understand and maintain.

### Code with Comments

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        combinedIntervals = []
        newStart, newEnd = newInterval
        i = 0
        n = len(intervals)

        # Add all intervals that come before the new interval
        while i < n and intervals[i][1] < newStart:
            combinedIntervals.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        combinedIntervals.append([newStart, newEnd])

        # Add all intervals that come after the new interval
        while i < n:
            combinedIntervals.append(intervals[i])
            i += 1

        return combinedIntervals
```

