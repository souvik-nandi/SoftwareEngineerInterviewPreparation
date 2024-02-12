'''

Problem Statement: Groups of Special-Equivalent Strings

Link: https://leetcode.com/problems/groups-of-special-equivalent-strings
Tags: ['String']
Difficulty: Easy

You are given an array words of strings.
A move onto s consists of swapping any two even indexed characters of s, or any two odd indexed characters of s.
Two strings s and t are special-equivalent if after any number of moves onto s, s == t.
For example, s = "zzxy" and t = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz" that swap s[0] and s[2], then s[1] and s[3].
Now, a group of special-equivalent strings from words is a non-empty subset of words such that:

Every pair of strings in the group are special equivalent, and;
The group is the largest size possible (ie., there isn't a string s not in the group such that s is special equivalent to every string in the group)

Return the number of groups of special-equivalent strings from words.
 

Example 1:
Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation: 
One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings are all pairwise special equivalent to these.

The other two groups are ["xyzz", "zzxy"] and ["zzyx"].  Note that in particular, "zzxy" is not special equivalent to "zzyx".


Example 2:
Input: words = ["abc","acb","bac","bca","cab","cba"]
Output: 3
 






Note:

1 <= words.length <= 1000
1 <= words[i].length <= 20
All words[i] have the same length.
All words[i] consist of only lowercase letters.







'''

