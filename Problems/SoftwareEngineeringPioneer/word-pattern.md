# 290. Word Pattern

## Problem Description
Given a pattern and a string `s`, return `true` if `s` follows the same pattern. A string `s` follows the pattern if there is a one-to-one mapping between pattern characters and words in `s`.

### Example
- **Input:** `pattern = "abba", s = "dog cat cat dog"`
- **Output:** `True`

- **Input:** `pattern = "abba", s = "dog cat cat fish"`
- **Output:** `False`

## Solution
The improved solution uses two dictionaries to perform bidirectional mapping checks:

1. **Initialize Data Structures**
   - Use two dictionaries:
     - `wordPatternMap` to map words to pattern characters.
     - `patternWordMap` to map pattern characters to words.

2. **Check Mappings**
   - For each character in the pattern and corresponding word:
     - Ensure that the word maps to the expected pattern character and vice versa.
     - If any inconsistency is found, return `False`.

3. **Return Result**
   - If all checks pass, return `True`.

### Complexity
- **Time Complexity:** `O(n)`, where `n` is the number of characters in the pattern or words in the string.
- **Space Complexity:** `O(n)`, due to the space required for the dictionaries.

### Code

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string s into words
        words = s.split()

        # Check if the number of words matches the number of characters in the pattern
        if len(words) != len(pattern):
            return False
        
        # Dictionaries for bidirectional mapping
        wordPatternMap = {}
        patternWordMap = {}

        # Iterate over each character in the pattern and corresponding word
        for c, word in zip(pattern, words):
            # Check if the current mappings are consistent
            if (word in wordPatternMap and wordPatternMap[word] != c) or (c in patternWordMap and patternWordMap[c] != word):
                return False
            # Map the word to the pattern character and vice versa
            wordPatternMap[word] = c
            patternWordMap[c] = word
        
        # If all checks pass, the pattern matches
        return True
```

## Comparison

- **Original Approach:** Uses a single dictionary and a set for checking one-directional mapping.
  - **Pros:** Simple and easy to understand.
  - **Cons:** Less comprehensive, may miss cases where the pattern character is reused.

- **Improved Approach:** Uses two dictionaries to ensure bidirectional mapping.
  - **Pros:** Comprehensive and handles edge cases better by checking both directions.
  - **Cons:** Slightly more space usage, but the robustness outweighs the cost.

### Conclusion
The improved solution with bidirectional mapping is preferred for its comprehensive check and better handling of edge cases. It provides a more robust and reliable solution to the problem.
