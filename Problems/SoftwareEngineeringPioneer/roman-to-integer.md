## 13. Roman to Integer

Given a Roman numeral string `s`, convert it to an integer. The Roman numeral system includes the following symbols:

- **I** = 1
- **V** = 5
- **X** = 10
- **L** = 50
- **C** = 100
- **D** = 500
- **M** = 1000

Roman numerals are usually written largest to smallest from left to right. However, there are exceptions, where a smaller numeral precedes a larger numeral to indicate subtraction. For example, "IV" represents 4 (5 - 1) instead of 6 (1 + 5).

### Examples:

- **Input:** `s = "III"`  
  **Output:** `3`

- **Input:** `s = "IV"`  
  **Output:** `4`

- **Input:** `s = "IX"`  
  **Output:** `9`

- **Input:** `s = "LVIII"`  
  **Output:** `58`

- **Input:** `s = "MCMXCIV"`  
  **Output:** `1994`

## Solution Explanation

### Approach

The solution iterates through the string while maintaining a total sum. It uses a dictionary to map Roman numeral characters to their corresponding integer values. During iteration, it compares each character with the next one:

- If the current character's value is less than the next character's value, it subtracts the current value from the total (to handle cases like "IV").
- Otherwise, it adds the current value to the total.

### Time Complexity

- **O(n)**: The algorithm processes each character in the string exactly once, making it linear with respect to the length of the input string.

### Space Complexity

- **O(1)**: The algorithm uses a fixed amount of space regardless of the input size. The dictionary and a few integer variables occupy constant space.

### Python Implementation

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # Map of Roman numerals to integer values
        romanToIntMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # Initialize total sum
        n = len(s)  # Length of the input string
        idx = 0  # Current index

        while idx < n:
            curVal = romanToIntMap[s[idx]]  # Value of the current character
            nextVal = romanToIntMap[s[idx + 1]] if idx < n - 1 else 0  # Value of the next character (or 0 if none)

            if curVal < nextVal:
                total -= curVal  # Subtract if the current value is less than the next
            else:
                total += curVal  # Otherwise, add the current value
            
            idx += 1  # Move to the next character
        
        return total
```

### Commentary

- **Efficiency:** This implementation is already optimized with an O(n) time complexity and O(1) space complexity. Each character in the string is visited exactly once.
  
- **Edge Cases:** The algorithm correctly handles edge cases, such as the smallest Roman numeral ("I"), and strings that include subtractive combinations like "IV" and "IX".

## Alternative Solutions

### Alternative 1: Reverse Traversal with Single Pass

Another approach is to traverse the string from right to left. Instead of comparing the current numeral with the next one, you compare it with the previous one (from the reversed perspective). If the current numeral is less than the previous one, you subtract; otherwise, you add.

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = romanToIntMap[s[-1]]  # Start with the last character's value
        n = len(s)
        
        for i in range(n - 2, -1, -1):  # Traverse from second-last to the first character
            if romanToIntMap[s[i]] < romanToIntMap[s[i + 1]]:
                total -= romanToIntMap[s[i]]  # Subtract if the current value is less than the next
            else:
                total += romanToIntMap[s[i]]  # Otherwise, add the current value
        
        return total
```

### Comparison with the Original Solution

- **Performance:** Both the original and alternative solutions have the same time and space complexity (O(n) and O(1) respectively). Therefore, neither is fundamentally faster in big-O terms.
- **Readability:** The original solution is more intuitive, especially for those familiar with Roman numeral rules, as it directly matches the reading order.
- **Edge Cases:** Both handle edge cases similarly.

### Conclusion

The original solution is optimal and easy to understand. The alternative solution, while also efficient, may be slightly less intuitive because it traverses the string in reverse. However, both approaches are valid and perform well for the given problem.
