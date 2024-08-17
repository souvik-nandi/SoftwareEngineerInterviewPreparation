# 205. Isomorphic Strings

## Problem Description
Given two strings `s` and `t`, determine if they are isomorphic. Two strings are isomorphic if the characters in `s` can be replaced to get `t`, with each character mapping to exactly one other character and vice versa.

### Example 1
- **Input:** `s = "egg", t = "add"`
- **Output:** `True`

### Example 2
- **Input:** `s = "foo", t = "bar"`
- **Output:** `False`

## Solution
The solution uses two dictionaries to track character mappings between the two strings.

### Algorithm

1. **Initialize Two Dictionaries**
   - `s2tCharMap` to track mappings from characters in `s` to characters in `t`.
   - `t2sCharMap` to track mappings from characters in `t` to characters in `s`.

2. **Iterate Through Characters**
   - For each pair of characters from `s` and `t`:
     - Check if the current character from `s` (`sChar`) is already mapped to a different character in `t`. If yes, return `False`.
     - Similarly, check if the current character from `t` (`tChar`) is already mapped to a different character in `s`. If yes, return `False`.
     - If no inconsistency is found, update the mappings.

3. **Return True**
   - If no inconsistencies are found during the iteration, return `True`.

### Complexity
- **Time Complexity:** `O(n)`, where `n` is the length of the strings. The solution involves a single pass through the characters of both strings, making it linear.
- **Space Complexity:** `O(n)`, due to the storage required for the two dictionaries.

### Code

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionaries to track character mappings from s to t and t to s
        s2tCharMap = {}
        t2sCharMap = {}

        # Iterate through characters of both strings
        for sChar, tChar in zip(s, t):
            # Check if there's an existing mapping in s2tCharMap
            if sChar in s2tCharMap:
                # If there's a mismatch, the strings aren't isomorphic
                if s2tCharMap[sChar] != tChar:
                    return False
            # If no mapping exists, establish it
            else:
                s2tCharMap[sChar] = tChar

            # Check if there's an existing mapping in t2sCharMap
            if tChar in t2sCharMap:
                # If there's a mismatch, the strings aren't isomorphic
                if t2sCharMap[tChar] != sChar:
                    return False
            # If no mapping exists, establish it
            else:
                t2sCharMap[tChar] = sChar

        # If all mappings are consistent, the strings are isomorphic
        return True
```

## Alternative Solution
An alternative approach involves using a single dictionary and checking for character indices to ensure consistency:
- **Single Dictionary Approach:** 
  1. Use a single dictionary to track character mappings.
  2. Track the indices of each character to check for consistent mapping.

### Comparison

- **Original Approach:** Utilizes two dictionaries to manage bidirectional mappings between characters in `s` and `t`. This approach ensures that each character maps consistently in both directions and has a linear time complexity `O(n)`.

- **Alternative Approach:** Uses a single dictionary but requires additional checks for consistent mapping. This approach can also achieve `O(n)` time complexity but may be less intuitive due to the need for tracking indices.

### Conclusion
- **Efficiency:** The original approach with two dictionaries is straightforward and handles bidirectional character mapping clearly.
- **Simplicity:** The single dictionary approach is also effective but may be more complex to implement due to additional checks.

Both approaches are valid, and the choice may depend on implementation preference and readability.
