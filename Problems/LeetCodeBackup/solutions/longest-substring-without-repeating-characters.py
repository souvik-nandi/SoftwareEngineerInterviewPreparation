'''

Problem Statement: Longest Substring Without Repeating Characters

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters
Tags: ['Hash Table', 'Two Pointers', 'String', 'Sliding Window']
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.
 
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0

 
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.



'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        if s == "":
            return 0
        
        maxLength = 0
        charSet = {}
        start = 0
        end = 0
        
        for end in range(len(s)):
            # if the element is found in the map check whether it occurred before the starting index
            if s[end] in charSet and charSet[s[end]] >= start:
                # if the repeating element occured after the start then the start should be positioned at start + 1 so that there are no duplicates
                start = charSet[s[end]] + 1
            
            charSet[s[end]] = end
            maxLength = max(end - start + 1, maxLength)
        
        return maxLength
    