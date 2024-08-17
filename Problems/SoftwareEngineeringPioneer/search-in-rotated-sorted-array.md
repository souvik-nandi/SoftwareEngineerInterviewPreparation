## 33. Search in Rotated Sorted Array

You are given an integer array `nums` sorted in ascending order, but the array is rotated at some pivot index. You are also given an integer `target`. Write a function to search for `target` in the rotated array and return its index. If `target` is not found, return `-1`.


### Problem Examples

#### Example 1
- **Input:** `nums = [4,5,6,7,0,1,2], target = 0`
- **Output:** `4`

#### Example 2
- **Input:** `nums = [4,5,6,7,0,1,2], target = 3`
- **Output:** `-1`

### Solution
The solution involves two main functions:

1. **`findMin(nums: List[int]) -> int`**
   - Finds the index of the smallest element in the rotated array, which is also the pivot point where the rotation happened.
   
2. **`search(nums: List[int], target: int) -> int`**
   - Uses the index of the smallest element to adjust the standard binary search for a rotated sorted array.

### Algorithm

1. **Finding the Minimum Element (Pivot)**
   - Use binary search to locate the pivot index. The pivot is where the rotation happened, and the smallest element in the array.
   - Handle edge cases where the array is empty or consists of a single element.

2. **Searching for the Target**
   - Determine the pivot point.
   - Adjust the binary search to account for the rotation by calculating the real index considering the pivot.

### Complexity
- **Time Complexity:** `O(log n)`, where `n` is the number of elements in the array. Both finding the minimum and searching are `O(log n)` operations.
- **Space Complexity:** `O(1)`, as no additional space is used apart from the input variables.

### Code

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Edge cases for empty array or single element
        if not nums:
            return -1
        if len(nums) == 1 or nums[0] < nums[-1]:
            return 0  # Return index 0 since the array is already sorted

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If the middle element is smaller than its previous one, it's the minimum
            if nums[mid] < nums[mid - 1]:
                return mid
            
            # Decide whether to search in the left or right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left  # The minimum is found when left == right

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Find the index of the minimum element (i.e., the pivot point)
        pivot = self.findMin(nums)

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            # Calculate the real mid considering the rotation (pivot)
            realMid = (mid + pivot) % n

            if nums[realMid] == target:
                return realMid
            elif nums[realMid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # Target not found
```

### Alternative Solution
An alternative approach involves a single binary search by checking the middle element and adjusting the search space based on the position of the target relative to the middle and pivot points. This approach may have a different implementation but achieves the same `O(log n)` time complexity.

### Comparison
- **Original Approach:** Uses a two-step process: first finding the pivot and then performing a binary search on the adjusted indices.
- **Alternative Approach:** May involve directly adjusting the binary search based on the rotation, potentially simplifying the process but generally has similar time complexity.

Both approaches are efficient and suitable for the problem constraints. The choice between them may depend on specific use cases or implementation preferences.
