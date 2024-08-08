# 58. Length of Last Word

## Problem Statement

Given a string `s` consisting of words and spaces, return the length of the last word in the string. A word is defined as a maximal substring consisting of non-space characters only.

### Example

**Input:**
```
s = "Hello World  "
```
**Output:**
```
5
```

**Explanation:** The last word in the string is "World", which has a length of 5.

## Solution: Manual Traversal Without Inbuilt Functions

### Algorithm Description

The solution manually traverses the string to identify the last word and calculate its length without relying on any inbuilt functions. Here's how it works:

1. **Skip Trailing Spaces**: The algorithm starts from the end of the string and moves backward, skipping any trailing spaces.
2. **Count the Length of the Last Word**: Once the end of the last word is found (i.e., after skipping spaces), it counts the number of characters until it encounters another space or the start of the string.

### Key Details

- **Manual Traversal**: The algorithm avoids using any inbuilt functions like `rstrip()` or `split()`, making it a pure manual implementation.
- **Efficiency**: The solution processes the string in a single pass from the end, ensuring it only examines the necessary part of the string.

### Complexity

- **Time Complexity**: O(n), where `n` is the length of the string. The string is traversed at most twice: once to skip trailing spaces and once to count the last word.
- **Space Complexity**: O(1), since only a few variables are used to store the length and indices.

## Conclusion

This solution efficiently computes the length of the last word in a string by directly manipulating the string without using any additional inbuilt functions. It ensures minimal overhead and maintains a linear time complexity, making it suitable for environments with constraints on using library functions.

### Code with Comments

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        end = n - 1

        # Skip trailing spaces
        while end >= 0 and s[end] == ' ':
            end -= 1

        # Count the length of the last word
        length = 0
        while end >= 0 and s[end] != ' ':
            length += 1
            end -= 1
        
        return length
```
