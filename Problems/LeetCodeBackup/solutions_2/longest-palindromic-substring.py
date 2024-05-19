'''

Problem Statement: Longest Palindromic Substring

Link: https://leetcode.com/problems/longest-palindromic-substring
Tags: ['String', 'Dynamic Programming']
Difficulty: Medium

Given a string s, return the longest palindromic substring in s.
 
Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),



'''


# O(n^2) algorithm which is an acceptable approach but there also exists
# an O(n) linear time complexity algorithm

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def findPalindromeLength(ptr1, ptr2, s, n): 
            start = 0
            end = -1
            
            while ptr1 >= 0 and ptr2 < n and s[ptr1] == s[ptr2]:
                start = ptr1
                end = ptr2
                ptr1 -= 1
                ptr2 += 1

            return start, end
        
        n = len(s)
        maxPalindrome = ""
        maxPalindromeLength = 0
        
        for i in range(n):
            start1, end1 = findPalindromeLength(i, i, s, n)
            start2, end2 = findPalindromeLength(i, i+1, s, n)
            start, end = [start1, end1] if (end1 - start1) > (end2 - start2) else [start2, end2]
            
            if ((end - start + 1) > maxPalindromeLength):
                maxPalindrome = s[start:end+1]
                maxPalindromeLength = end - start + 1
            
        
        return maxPalindrome


# O(n) solution
# Manachers algorithm

