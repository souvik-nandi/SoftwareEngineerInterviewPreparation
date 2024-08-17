## 20. Valid Parentheses

Given a string `s` containing just the characters `'(', ')', '{', '}', '['`, and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Problem Examples

#### Example 1:
- **Input:** `s = "()"`  
- **Output:** `true`
- **Explanation:** The string has one pair of matching parentheses, which is valid.

#### Example 2:
- **Input:** `s = "()[]{}"`  
- **Output:** `true`
- **Explanation:** The string contains multiple matching pairs of parentheses, brackets, and braces, all in the correct order.

#### Example 3:
- **Input:** `s = "(]"`  
- **Output:** `false`
- **Explanation:** The string has mismatched parentheses and brackets.

### Possible Solutions

1. **Stack-Based Validation**

### Solution 1: Stack-Based Validation

```python
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in bracket_map:
                if not stack or stack.pop() != bracket_map[c]:
                    return False
            else:
                stack.append(c)
                
        return not stack
```

#### Algorithm Description

1. **Mapping Brackets**:
   - A dictionary `bracket_map` is used to store mappings of closing to opening brackets: `')': '(', '}': '{', ']': '['`.

2. **Using a Stack**:
   - A stack is used to track opening brackets. As we iterate through the string `s`, the following steps occur:
     - If the character is a closing bracket (i.e., it is in `bracket_map`), check if the stack is non-empty and if the top of the stack matches the corresponding opening bracket.
     - If the stack is empty or the top of the stack doesn't match, return `False` immediately, as the string is invalid.
     - If the character is an opening bracket, it is pushed onto the stack.
   
3. **Final Validation**:
   - After processing all characters, the string is valid only if the stack is empty. An empty stack means that all opening brackets had corresponding closing brackets in the correct order.

#### Complexity Analysis

- **Time Complexity**: `O(n)`
  - The algorithm processes each character in the string exactly once, making it linear in terms of the number of characters `n`.

- **Space Complexity**: `O(n)`
  - The worst-case space complexity occurs when all characters in the string are opening brackets, in which case the stack will contain all `n` characters.

#### Potential Pitfalls

1. **Unmatched Brackets**:
   - If the string has unmatched opening or closing brackets, the stack will not be empty at the end, leading to a `False` result.

2. **Empty String**:
   - An empty string is considered valid since there are no unmatched brackets.

3. **Early Termination**:
   - The algorithm efficiently terminates early if a closing bracket doesn't have a corresponding opening bracket in the stack, avoiding unnecessary further computation.

### Conclusion

The stack-based approach is an optimal solution for validating parentheses and other types of brackets in a string. It effectively ensures that brackets are closed in the correct order and that every opening bracket has a corresponding closing bracket. The time and space complexities are both linear, making this solution efficient and scalable for longer strings.
