## 9. Palindrome Number

The problem is to determine whether a given integer `x` is a palindrome. A palindrome is a number that reads the same forward and backward. For example, `121` is a palindrome, while `123` is not.

## Problem Examples

**Example 1:**

- **Input:** `x = 121`
- **Output:** `True`
- **Explanation:** `121` reads the same forward and backward, so it is a palindrome.

**Example 2:**

- **Input:** `x = -121`
- **Output:** `False`
- **Explanation:** `-121` reads as `121-` backward, so it is not a palindrome.

**Example 3:**

- **Input:** `x = 10`
- **Output:** `False`
- **Explanation:** `10` reads as `01` backward, so it is not a palindrome.

## Possible Solutions

### Solution 1: Reversing Half of the Number

This approach determines if the integer is a palindrome by reversing the second half of the number and comparing it to the first half. By doing this, we avoid potential issues related to integer overflow and unnecessary full reversal.

#### Code:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # When x is negative, it cannot be a palindrome
        # When the last digit is 0, the number cannot be a palindrome unless the number is 0 itself
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversedHalf = 0
        while x > reversedHalf:
            reversedHalf = reversedHalf * 10 + x % 10
            x //= 10

        # When the length is odd, we can ignore the middle digit by reversedHalf//10
        return x == reversedHalf or x == reversedHalf // 10
```

### Algorithm Description:

1. **Edge Cases:**
   - If `x` is negative or ends with a `0` (and `x` is not `0` itself), the function returns `False` as such numbers cannot be palindromes.

2. **Reversing the Second Half of the Number:**
   - The algorithm repeatedly extracts the last digit of `x` and appends it to `reversedHalf` while simultaneously removing that digit from `x`.
   - The loop continues until `reversedHalf` is greater than or equal to `x`, ensuring that we have reversed at least half of the number.

3. **Checking for Palindrome:**
   - Finally, the function checks if either `x` is equal to `reversedHalf` (for even-length numbers) or `x` is equal to `reversedHalf // 10` (for odd-length numbers where the middle digit doesn't matter).

### Complexity Analysis:

- **Time Complexity:** `O(log_{10}(n))` - The time complexity is logarithmic with respect to the number of digits in `x`, as we're effectively processing the number digit by digit.
- **Space Complexity:** `O(1)` - The algorithm uses a constant amount of space.

### Potential Pitfalls:

- This solution is efficient and avoids problems with integer overflow that might occur in languages with fixed-precision integers. However, it might not be intuitive to understand for beginners.

### Alternative Solution: Full Number Reversal

**Algorithm Description:**
- An alternative solution is to reverse the entire number and then compare it with the original number.

**Code:**

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversedNum = 0

        while x > 0:
            reversedNum = reversedNum * 10 + x % 10
            x //= 10
        
        return original == reversedNum
```

**Complexity Analysis:**
- **Time Complexity:** `O(log_{10}(n))` - The time complexity remains logarithmic, as it still processes the number digit by digit.
- **Space Complexity:** `O(1)` - The space complexity is constant.

**Drawbacks:**
- This method is simpler to understand but less optimal than the half-reversal method. It may also suffer from overflow issues in languages without arbitrary precision integers.

### Conclusion

The half-reversal method is generally better because it avoids reversing the entire number, thus optimizing performance and reducing potential edge cases related to overflow. The full reversal method, though more intuitive, is slightly less efficient and should be considered when simplicity is prioritized over optimality.
