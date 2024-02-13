# 3. Longest Substring Without Repeating Characters

## Problem

Longest Substring Without Repeating Characters

`Medium`

Given a string s, find the length of the longest
substring without repeating characters.

Example 1:

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

Example 2:

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

Constraints:

`0 <= s.length <= 5 * 10^4`
`s` consists of English letters, digits, symbols and spaces.

# Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the index of the last occurrence of each character
        charIndex = {}
        # Variable to track the maximum length of the substring without repeating characters
        maxLen = 0
        # Variable to track the start index of the current substring
        start = 0

        # Loop through each character in the string along with its index
        for i, c in enumerate(s):
            # If the current character is already in the dictionary and its last occurrence
            # index is after the start of the current substring, update the start index
            if c in charIndex and charIndex[c] >= start:
                start = charIndex[c] + 1

            # Update the index of the current character in the dictionary
            charIndex[c] = i
            # Update the maximum length of the substring
            maxLen = max(maxLen, i - start + 1)

        # Return the maximum length of the substring without repeating characters
        return maxLen
```
