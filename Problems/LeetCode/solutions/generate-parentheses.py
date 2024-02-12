'''

Problem Statement: Generate Parentheses

Link: https://leetcode.com/problems/generate-parentheses
Tags: ['String', 'Backtracking']
Difficulty: Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]

 
Constraints:

1 <= n <= 8

'''

from typing import List

'''
Solution 1 is a recursive solution.
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 0:
            return []

        parenthesis_list = []
        
        def add_parenthesis(cur_item, current_open, current_closed):
            if current_open == n and current_closed == n:
                parenthesis_list.append(cur_item)
                return

            if current_open < n:
                add_parenthesis(cur_item + "(", current_open + 1, current_closed)
            if current_closed < n and current_open > current_closed:
                add_parenthesis(cur_item + ")", current_open, current_closed + 1)
            
        add_parenthesis("", 0, 0)
        
        return parenthesis_list
