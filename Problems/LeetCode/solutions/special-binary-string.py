'''

Problem Statement: Special Binary String

Link: https://leetcode.com/problems/special-binary-string
Tags: ['String', 'Recursion']
Difficulty: Hard

Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.

Given a special string s, a move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)
At the end of any number of moves, what is the lexicographically largest resulting string possible?
Example 1:
Input: s = "11011000"
Output: "11100100"
Explanation:
The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

Note:

s has length at most 50.
s is guaranteed to be a special binary string as defined above.



'''

