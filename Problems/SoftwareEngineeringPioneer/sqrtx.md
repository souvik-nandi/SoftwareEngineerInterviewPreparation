# 69. Sqrt(x)

## Problem Description
Given a non-negative integer `x`, compute and return the square root of `x`. Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

### Example
```python
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we truncate the decimal part, 2 is returned.
```

## Solution 1: Binary Search (Original Solution)

### Code
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x // 2

        while start <= end:
            mid = (start + end) // 2

            preVal = mid * mid
            nxtVal = (mid + 1) * (mid + 1)

            if preVal == x or preVal < x < nxtVal:
                return mid
            elif nxtVal == x:
                return mid + 1
            elif preVal > x:
                end = mid - 1
            else:
                start = mid + 1
        
        return 0
```

### Algorithm Description
- **Step 1**: Initialize `start` to 0 and `end` to `x // 2` (as the square root of `x` will never be more than `x // 2` for `x >= 4`).
- **Step 2**: Use binary search to find the integer square root of `x`.
  - Calculate `mid` as the midpoint between `start` and `end`.
  - Calculate `preVal` as `mid * mid` and `nxtVal` as `(mid + 1) * (mid + 1)`.
  - If `preVal` is equal to `x` or `preVal < x < nxtVal`, return `mid`.
  - If `nxtVal` is equal to `x`, return `mid + 1`.
  - If `preVal` is greater than `x`, search the left half by updating `end`.
  - If `preVal` is less than `x`, search the right half by updating `start`.
- **Step 3**: Return 0 if no exact or close match is found (edge case).

### Complexity Analysis
- **Time Complexity**: `O(log x)` - The binary search reduces the search space logarithmically.
- **Space Complexity**: `O(1)` - Constant space is used.

## Solution 2: Optimized Binary Search

### Code
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            mid = (left + right) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return right
```

### Algorithm Description
- **Step 1**: Handle small values of `x` (0 and 1) by returning `x` directly.
- **Step 2**: Initialize `left` to 2 and `right` to `x // 2`.
- **Step 3**: Use binary search to find the integer square root of `x`.
  - Calculate `mid` as the midpoint between `left` and `right`.
  - Calculate `num` as `mid * mid`.
  - If `num` equals `x`, return `mid`.
  - If `num` is greater than `x`, search the left half by updating `right`.
  - If `num` is less than `x`, search the right half by updating `left`.
- **Step 4**: Return `right` as the truncated integer square root.

### Complexity Analysis
- **Time Complexity**: `O(log x)` - The binary search still reduces the search space logarithmically.
- **Space Complexity**: `O(1)` - Constant space is used.

## Solution 3: Newton's Method (Newton-Raphson)

### Code
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        # Start with an initial guess.
        guess = x
        while True:
            # Apply Newton's method formula.
            next_guess = (guess + x // guess) // 2
            
            # If the guess stabilizes, return it.
            if next_guess >= guess:
                return guess
            guess = next_guess
```

### Algorithm Description
- **Step 1**: Handle the edge case for `x = 0` by returning `0`.
- **Step 2**: Start with an initial guess equal to `x`.
- **Step 3**: Apply Newton's method iteratively:
  - Calculate the next guess as `(guess + x // guess) // 2`.
  - If the next guess is greater than or equal to the current guess, return the current guess (stabilization condition).
  - Otherwise, update the guess and continue.
- **Step 4**: Continue until the guess stabilizes, then return the integer square root.

### Complexity Analysis
- **Time Complexity**: `O(log x)` - Newton's method converges very quickly, typically in `O(log x)` iterations.
- **Space Complexity**: `O(1)` - Only a few variables are used, making the space complexity constant.

## Comparison

- **Efficiency**:
  - **Binary Search (Original)**: `O(log x)` time and `O(1)` space. Good, but a bit verbose.
  - **Optimized Binary Search**: `O(log x)` time and `O(1)` space. Simplified logic and improved handling of small inputs.
  - **Newton's Method**: `O(log x)` time and `O(1)` space. Newton's method often converges faster than binary search, making it more efficient in practice.
  
- **Code Complexity**:
  - **Binary Search (Original)**: More code and additional checks, making it slightly harder to understand.
  - **Optimized Binary Search**: Cleaner and more straightforward, easier to read and maintain.
  - **Newton's Method**: Shortest and most elegant, but it requires understanding of numerical methods.

**Conclusion**: Newton's Method is the most efficient and elegant solution for this problem. It typically converges faster than binary search and uses a simple iterative approach. The optimized binary search is also a strong choice with a balance between simplicity and performance.
