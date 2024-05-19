'''

Problem Statement: Letter Combinations of a Phone Number

Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number
Tags: ['String', 'Backtracking', 'Depth-first Search', 'Recursion']
Difficulty: Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

 
Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

'''

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        def product(args):
            if len(args) == 0:
                return []
            result = args[0]
            for pool in args[1:]:
                result = [x+y for x in result for y in pool]
            return result
        
        digits_map = {
            '1': [' '],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [' '],
        }
        
        combs = product([digits_map[digit] for digit in digits])  
        
        return combs
