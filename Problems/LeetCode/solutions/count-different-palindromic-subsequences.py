'''

Problem Statement: Count Different Palindromic Subsequences

Link: https://leetcode.com/problems/count-different-palindromic-subsequences
Tags: ['String', 'Dynamic Programming']
Difficulty: Hard

Given a string s, find the number of different non-empty palindromic subsequences in s, and return that number modulo 10^9 + 7.
A subsequence of a string s is obtained by deleting 0 or more characters from s.
A sequence is palindromic if it is equal to the sequence reversed.
Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.
Example 1:
Input: 
s = 'bccb'
Output: 6
Explanation: 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

Example 2:
Input: 
s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation: 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

Note:

The length of s will be in the range [1, 1000].
Each character s[i] will be in the set {'a', 'b', 'c', 'd'}.



'''

