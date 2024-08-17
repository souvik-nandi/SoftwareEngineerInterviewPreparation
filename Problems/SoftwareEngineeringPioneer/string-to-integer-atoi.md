# 8. String to Integer (atoi)

## Problem Statement

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function). The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the function. If the first sequence of non-whitespace characters in `s` is not a valid integral number or if no such sequence exists because either `s` is empty or it contains only whitespace characters, no conversion is performed, and the function returns `0`.

Note:

- Only the space character `' '` is considered a whitespace character.
- Assume the environment does not allow storing 64-bit integers (signed or unsigned).

The function returns:

- The integer represented by the string.
- `INT_MAX` (2^31 − 1) if the number is greater than the maximum 32-bit signed integer.
- `INT_MIN` (−2^31) if the number is less than the minimum 32-bit signed integer.

### Example

**Input:**
```
s = "42"
```
**Output:**
```
42
```

**Input:**
```
s = "   -42"
```
**Output:**
```
-42
```

**Input:**
```
s = "4193 with words"
```
**Output:**
```
4193
```

**Input:**
```
s = "words and 987"
```
**Output:**
```
0
```

## Solution: Iterative Parsing Approach

### Algorithm Description

This solution involves parsing the string character by character, extracting and converting the relevant portion into an integer, and handling edge cases like overflow and non-numeric characters.

1. **Initialize**:
    - A dictionary `numbersMap` maps character digits to their numeric values.
    - A dictionary `signsMap` maps '+' to `+1` and '-' to `-1`.
    - Initialize variables `index` to traverse the string, and `n` to store the string's length.
  
2. **Skip Leading Whitespace**:
    - Increment the `index` to skip over any leading whitespace.

3. **Determine Sign**:
    - Check if the current character is a sign (`'+'` or `'-'`). If so, update the `sign` variable accordingly and increment `index`.

4. **Convert Characters to Integer**:
    - Loop through the numeric characters, multiplying the current `number` by 10 and adding the corresponding numeric value.
    - Check for overflow and return `INT_MAX` or `INT_MIN` accordingly.

5. **Return Result**:
    - Multiply the `number` by `sign` and return the final result.

### Complexity

- **Time Complexity**: O(n), where `n` is the length of the string. Each character is processed at most once.
- **Space Complexity**: O(1), no additional space other than a few variables is used.

### Edge Cases

- Handling overflow and underflow situations.
- Strings with leading whitespace.
- Strings that start with non-numeric characters.
- Empty strings or strings with only whitespace.

### Code Implementation with Comments

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        # Maps digit characters to their corresponding integer values
        numbersMap = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }
        # Maps signs to their respective integer multipliers
        signsMap = { '-': -1, '+': 1 }
        
        index, n = 0, len(s)
        
        # Skip leading whitespace
        while index < n and s[index] == ' ':
            index += 1

        # Check if the next character is a sign
        if index < n and (s[index] == '-' or s[index] == '+'):
            sign = signsMap[s[index]]  # Assign the correct sign
            index += 1
        else:
            sign = 1  # Default sign is positive

        number = 0
        # Convert the numeric part of the string
        while index < n and s[index] in numbersMap:
            # Accumulate the number digit by digit
            number = number * 10 + numbersMap[s[index]]
            index += 1
            
            # Check for 32-bit integer overflow and underflow
            if sign * number > 2147483647:
                return 2147483647  # INT_MAX
            if sign * number < -2147483648:
                return -2147483648  # INT_MIN

        # Return the final number with the appropriate sign
        return sign * number
```

### Conclusion

This solution efficiently handles various edge cases and constraints, including leading whitespace, sign detection, numeric conversion, and overflow/underflow checks. By avoiding the use of any built-in functions except basic string indexing, it closely mimics the behavior of the `atoi` function in low-level languages like C/C++.