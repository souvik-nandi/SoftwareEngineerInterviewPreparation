# 56. Merge Intervals

## Problem Description

Given a collection of intervals, where each interval is represented by a pair of integers `[start, end]`, the goal is to merge all overlapping intervals and return a list of non-overlapping intervals that cover all the intervals in the input.

## Problem Examples

### Example 1

**Input:**

```python
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
```

**Output:**

```python
[[1, 6], [8, 10], [15, 18]]
```

**Explanation:**

- The intervals `[1, 3]` and `[2, 6]` overlap, so they are merged into `[1, 6]`.
- The intervals `[8, 10]` and `[15, 18]` do not overlap with each other.

### Example 2

**Input:**

```python
intervals = [[1, 4], [4, 5]]
```

**Output:**

```python
[[1, 5]]
```

**Explanation:**

- The intervals `[1, 4]` and `[4, 5]` overlap, so they are merged into `[1, 5]`.

## Possible Solutions

### Solution 1: Sorting and Merging

#### Code

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by the start of each interval
        intervals.sort(key=lambda x: x[0])

        merged = []
        current_start, current_end = intervals[0]
        pos = 1
        n = len(intervals)

        while pos < n:
            start, end = intervals[pos]

            if current_end >= start:  # Overlapping intervals
                current_end = max(current_end, end) # Only setting current_end and not current_start because it is already sorted
            else:
                merged.append([current_start, current_end])
                current_start, current_end = start, end
            
            pos += 1

        merged.append([current_start, current_end])

        return merged
```

#### Algorithm Description

1. **Sort Intervals**: The list of intervals is sorted by the starting times. This ensures that we can process intervals in sequential order and only need to compare the current interval with the next one.
   
2. **Merge Intervals**: Iterate through the sorted intervals:
   - If the current interval overlaps with the last merged interval (i.e., its start time is less than or equal to the end time of the last merged interval), update the end time of the last merged interval.
   - Otherwise, add the last merged interval to the result list and start a new interval.

3. **Append Last Interval**: After processing all intervals, append the last interval to the merged list.

#### Complexity Analysis

- **Time Complexity**: \(O(n \log n)\) due to the sorting step, where \(n\) is the number of intervals.
- **Space Complexity**: \(O(n)\) for storing the merged intervals.

#### Potential Pitfalls

- **Empty Input**: The function handles an empty list of intervals gracefully by returning an empty list.
- **Boundary Conditions**: Ensure that intervals with the same start or end times are handled correctly by the merging logic.

## Conclusion

This solution efficiently merges overlapping intervals by sorting the intervals and then merging them in a single pass. It is optimal for scenarios where the intervals are not pre-sorted and guarantees that all overlapping intervals are merged correctly.
