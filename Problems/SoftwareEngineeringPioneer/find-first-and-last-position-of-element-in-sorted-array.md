## 34. Find First and Last Position of Element in Sorted Array

Given a sorted array of integers `nums` and a target value `target`, return the starting and ending position of `target` in an array. If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

### Problem Examples

#### Example 1:
- **Input:** `nums = [5,7,7,8,8,10]`, `target = 8`
- **Output:** `[3,4]`
- **Explanation:** The target value `8` is found at positions 3 and 4.

#### Example 2:
- **Input:** `nums = [5,7,7,8,8,10]`, `target = 6`
- **Output:** `[-1,-1]`
- **Explanation:** The target value `6` is not found in the array.

#### Example 3:
- **Input:** `nums = []`, `target = 0`
- **Output:** `[-1,-1]`
- **Explanation:** The target value `0` is not found in an empty array.

### Possible Solutions

1. **Binary Search for First and Last Position**
2. **Linear Scan Approach**
3. **Single Pass Modified Binary Search**

### Solution 1: Binary Search for First and Last Position

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirstPosition(nums, target):
            left, right = 0, len(nums) - 1
            position = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    position = mid
                    right = mid - 1  # Narrow down to the left half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return position
        
        def findLastPosition(nums, target, start):
            left, right = start, len(nums) - 1
            position = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    position = mid
                    left = mid + 1  # Narrow down to the right half
                else:
                    right = mid - 1
            
            return position
        
        start = findFirstPosition(nums, target)
        if start == -1:  # Early exit if the target is not found
            return [-1, -1]
        
        end = findLastPosition(nums, target, start)
        
        return [start, end]
```

#### Algorithm Description

1. **Find First Position**:
   - A binary search is used to find the first occurrence of the target by adjusting the `right` pointer to narrow down the search to the left half whenever the target is found. The `position` is updated whenever the target is found.

2. **Find Last Position**:
   - Another binary search is used to find the last occurrence of the target by adjusting the `left` pointer to narrow down the search to the right half whenever the target is found. The search starts from the first found position (`start`), which reduces unnecessary comparisons.

3. **Final Return**:
   - If the target is found (`start != -1`), the first and last positions are returned. Otherwise, `[-1, -1]` is returned if the target is not found.

#### Complexity Analysis

- **Time Complexity**: `O(log n)`
  - Two binary searches are performed independently, both of which take `O(log n)` time.
  
- **Space Complexity**: `O(1)`
  - The algorithm uses a constant amount of extra space.

#### Potential Pitfalls

1. **Edge Cases**:
   - Ensure correct handling when the array is empty or when the target is not found.
   - Consider cases where all elements in the array are the same as the target or when the target is at the boundaries of the array.

2. **Off-by-One Errors**:
   - Careful consideration is required when adjusting the `left` and `right` pointers, especially when narrowing down to find the first and last occurrences.

### Solution 2: Linear Scan Approach

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i
                end = i
        
        return [start, end]
```

#### Algorithm Description

1. **Linear Scan**:
   - Iterate over the array to find the first and last occurrences of the target.
   - Start and end positions are updated as the target is encountered.

#### Complexity Analysis

- **Time Complexity**: `O(n)`
  - The algorithm scans each element in the array, leading to linear time complexity.
  
- **Space Complexity**: `O(1)`
  - The algorithm uses a constant amount of extra space.

#### Potential Pitfalls

1. **Efficiency**:
   - This solution is less efficient for large arrays compared to the binary search approach.

2. **Edge Cases**:
   - Similar edge cases as the binary search approach, such as an empty array or target not found, need to be considered.

### Solution 3: Single Pass Modified Binary Search

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, findFirst):
            left, right = 0, len(nums) - 1
            position = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    position = mid
                    if findFirst:
                        right = mid - 1  # Narrow down to the left half
                    else:
                        left = mid + 1  # Narrow down to the right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return position
        
        start = binarySearch(nums, target, True)
        if start == -1:
            return [-1, -1]
        end = binarySearch(nums, target, False)
        
        return [start, end]
```

#### Algorithm Description

1. **Single Pass Binary Search**:
   - A modified binary search is performed twice: once to find the first position and once to find the last position of the target. 
   - By toggling a flag `findFirst`, the search space is adjusted to either narrow down to the left half (for the first position) or to the right half (for the last position).

#### Complexity Analysis

- **Time Complexity**: `O(log n)`
  - Similar to the first solution, it performs two binary searches, each taking `O(log n)` time.
  
- **Space Complexity**: `O(1)`
  - The algorithm uses a constant amount of extra space.

#### Potential Pitfalls

1. **Edge Cases**:
   - Ensure that the edge cases are handled correctly, including when the target is not found or when the array is empty.
  
2. **Code Complexity**:
   - Although this approach is efficient, it may be slightly more complex to implement correctly due to the need to manage two different search scenarios within the same function.

### Conclusion

The **Binary Search for First and Last Position** solution and the **Single Pass Modified Binary Search** solution are both efficient and provide the desired `O(log n)` time complexity. The **Linear Scan Approach** is simpler but less efficient with a `O(n)` time complexity. 

- **Binary Search for First and Last Position** is preferred when you need a clear separation between finding the first and last positions.
- **Single Pass Modified Binary Search** can be slightly more efficient in practice, as it consolidates the logic into a single function but might be a bit more challenging to implement correctly.
- **Linear Scan Approach** is not recommended for large datasets due to its linear time complexity but could be considered when simplicity is more important than efficiency.
