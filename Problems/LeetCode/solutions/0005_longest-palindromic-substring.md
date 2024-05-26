# 5.

## Problem

## Solution

```Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Preprocess the string to insert special characters
        modified_s = '#' + '#'.join(s) + '#'
        n = len(modified_s)
        palindrome_lengths = [0] * n

        center = right = max_length = max_center = 0

        for i in range(n):
            # Calculate the mirror index of 'i' with respect to the center
            mirror = 2 * center - i

            if i < right:
                # If 'i' is within the right boundary, utilize symmetry property
                palindrome_lengths[i] = min(right - i, palindrome_lengths[mirror])

            # Attempt to expand palindrome centered at 'i'
            while (i - palindrome_lengths[i] - 1 >= 0 and
                i + palindrome_lengths[i] + 1 < n and
                modified_s[i - palindrome_lengths[i] - 1] == modified_s[i + palindrome_lengths[i] + 1]):
                palindrome_lengths[i] += 1

            # Update center and right boundary if needed
            if i + palindrome_lengths[i] > right:
                center = i
                right = i + palindrome_lengths[i]

            # Update max length and max center
            if palindrome_lengths[i] > max_length:
                max_length = palindrome_lengths[i]
                max_center = i

        start = (max_center - max_length) // 2
        return s[start:start + max_length]
```
