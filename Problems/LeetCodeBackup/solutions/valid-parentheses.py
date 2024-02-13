'''

Problem Statement: Valid Parentheses

Link: https://leetcode.com/problems/valid-parentheses
Tags: ['String', 'Stack']
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

 
Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.



'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets_map = { '(': ')', '{': '}', '[': ']' }
        opening_brackets = set(brackets_map.keys())
        isvalid = True
        
        for b in s:
            if b in opening_brackets:
                stack.append(b)
            else:
                if len(stack) == 0:
                    isvalid = False
                    break
                    
                o = stack.pop()
                if brackets_map[o] != b:
                    isvalid = False
                    break

            
        return len(stack) == 0 and isvalid

        