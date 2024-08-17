## 35. Search Insert Position

Given a sorted array of distinct integers `nums` and a target value `target`, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

### Problem Examples

#### Example 1:
- **Input:** `nums = [1,3,5,6]`, `target = 5`
- **Output:** `2`
- **Explanation:** `5` is found at index `2`.

#### Example 2:
- **Input:** `nums = [1,3,5,6]`, `target = 2`
- **Output:** `1`
- **Explanation:** `2` is not found, but would be inserted at index `1`.

#### Example 3:
- **Input:** `nums = [1,3,5,6]`, `target = 7`
- **Output:** `4`
- **Explanation:** `7` is not found, but would be inserted at index `4` (end of the list).

### Possible Solutions

1. **Binary Search with Insert Position Check**

### Solution 1: Binary Search with Insert Position Check

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0 or nums[0] > target:
            return 0
        elif nums[-1] < target:
            return n
        
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            curVal = nums[mid]
            leftVal = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            rightVal = nums[mid + 1] if mid + 1 < n else float('inf')

            if nums[mid] == target:
                return mid
            elif leftVal < target and target < curVal:
                return mid
            elif curVal < target and target < rightVal:
                return mid + 1
            elif curVal < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1
```

#### Algorithm Description

1. **Initial Edge Case Handling**:
   - If the array is empty (`n == 0`) or the first element is greater than the target (`nums[0] > target`), return `0` as the insertion point.
   - If the last element is less than the target (`nums[-1] < target`), return `n` as the insertion point (end of the array).

2. **Binary Search Loop**:
   - Initialize `left` pointer at the start of the array (`index 0`) and `right` pointer at the end (`index n-1`).
   - Calculate the middle index `mid` using `(left + right) // 2`.
   - Check three possible conditions:
     - If the middle value `nums[mid]` equals the target, return `mid`.
     - If the target lies between the previous value (`leftVal`) and the current middle value (`curVal`), return `mid`.
     - If the target lies between the current middle value (`curVal`) and the next value (`rightVal`), return `mid + 1`.
   - Adjust the `left` and `right` pointers based on the comparison between `curVal` and the target.

3. **Final Return**:
   - If the loop ends without finding the target, the function will return `-1`, although this case is theoretical and should not be reached.

#### Complexity Analysis

- **Time Complexity**: `O(log n)`
  - The algorithm performs a binary search, halving the search space each time.
  
- **Space Complexity**: `O(1)`
  - The algorithm uses a constant amount of extra space.

#### Potential Pitfalls

1. **Edge Cases**:
   - Ensure proper handling when the target is smaller than the smallest element or larger than the largest element.
   - Consider cases where the array has only one element or where the target would be inserted at the start or end of the array.

2. **Correctness of Index Calculations**:
   - The conditions that compare the target with `leftVal`, `curVal`, and `rightVal` must be carefully written to avoid off-by-one errors.

3. **Infinite Loop**:
   - Ensure that the loop correctly narrows down the search space, avoiding any scenario where the loop could run indefinitely.

### Conclusion

The Binary Search with Insert Position Check is an efficient solution to this problem, leveraging binary search to maintain `O(log n)` time complexity. This solution is effective for arrays where the position of insertion needs to be determined quickly. The careful handling of edge cases ensures that the solution is robust for a variety of inputs.
