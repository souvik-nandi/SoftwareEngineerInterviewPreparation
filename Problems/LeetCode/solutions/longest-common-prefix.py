'''

Problem Statement: Longest Common Prefix

Link: https://leetcode.com/problems/longest-common-prefix
Tags: ['String']
Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.



'''

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        min_len = min(len(str_item) for str_item in strs)
        
        if n == 0 or min_len == 0:
            return ""
        else:
            common_prefix = ""
            
            for index in range(min_len):
                char_set = set(str_item[index] for str_item in strs)
                
                if len(char_set) == 1:
                    common_prefix += strs[0][index]
                else:
                    return common_prefix
        
        return common_prefix
