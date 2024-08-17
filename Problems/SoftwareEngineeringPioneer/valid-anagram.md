# 242. Valid Anagram

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s` and `false` otherwise. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1
- **Input:** `s = "anagram", t = "nagaram"`
- **Output:** `True`

### Example 2
- **Input:** `s = "rat", t = "car"`
- **Output:** `False`

## Solution
The solution uses a fixed-size array to count the occurrences of each character in the two strings and then checks if the counts match.

### Algorithm

1. **Check Lengths**
   - If the lengths of `s` and `t` are different, they cannot be anagrams. Return `False`.

2. **Initialize a Count Array**
   - Create an array `count` of size 26 (for each letter of the English alphabet) initialized to 0.

3. **Count Characters**
   - Iterate through both strings simultaneously:
     - Increment the count for the character in `s`.
     - Decrement the count for the character in `t`.

4. **Check Counts**
   - If all counts are zero, the strings are anagrams. Otherwise, they are not.

### Complexity
- **Time Complexity:** `O(n)`, where `n` is the length of the strings. The solution involves a single pass through the strings.
- **Space Complexity:** `O(1)`, as the size of the `count` array is constant (26).

### Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Fixed-size array for counting characters (26 lowercase letters)
        count = [0] * 26

        # Count characters in both strings
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1  # Increment count for character in s
            count[ord(t[i]) - ord('a')] -= 1  # Decrement count for character in t

        # If all counts are zero, the strings are anagrams
        return all(c == 0 for c in count)
```

## Alternative Solution
Another approach is to use sorting to determine if two strings are anagrams:
- **Sorting Approach:**
  1. Sort both strings.
  2. Compare the sorted versions of the strings.

### Comparison

- **Original Approach:** Uses a fixed-size array to count characters. This approach has linear time complexity `O(n)` and constant space complexity `O(1)`. It is efficient in terms of both time and space.

- **Alternative Approach:** Sorting both strings has a time complexity of `O(n log n)` due to the sorting step and a space complexity of `O(1)` if sorting in place. This approach is straightforward but less efficient for larger strings compared to the counting approach.

### Conclusion
- **Efficiency:** The original approach with character counting is preferred for its linear time complexity and constant space usage. It is more efficient for large strings compared to sorting.
- **Simplicity:** The sorting approach is easier to understand but slower, making it suitable for cases where performance is less critical.

Both approaches are valid, but the character counting method is generally better for its efficiency.
