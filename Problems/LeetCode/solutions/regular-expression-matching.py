'''

Problem Statement: Regular Expression Matching

Link: https://leetcode.com/problems/regular-expression-matching
Tags: ['String', 'Dynamic Programming', 'Backtracking']
Difficulty: Hard

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
 
Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false

 
Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.



'''



'''
Solution:

The solution is provided through Dynamic Programming.

The initial idea is to check the match between smaller sets of the inputs.
For example if we consider the following inputs

s = "aab"
regex = "c*a*b"

we need to create two dimensional array and check the subsets of the problem.
In the first iteration check if 

s = "aab" -> sPartA = "a" , sPartB = "ab"
regex ="c*a*b" -> rPartA = "c" , rPartB = "*a*b"

sPartA and rPartA satisfies or not, and then gradually add each input and check.
   
A blank item is added for both string and regex to perform the dynamic programming using 2D array.

So we set dp[0][0] as True

If we take any item say dp[i][j] its value should define the following
    True -> s[0:i+1] satisfies regex[0:j+1]
    False -> s[0:i+1] does not satisfies regex[0:j+1]

If we can create this dp 2-D array, 
then the dp[sLen][rLen] value will give us the answer whether the input string and regex satisfies.

So, using the above inputs we can create the following dp array

        -   a   a   b
       [0] [1] [2] [3]
- [0] | T | F | F | F |
c [1] | F | F | F | F |
* [2] | T | F | F | F |
a [3] | F | T | F | F |
* [4] | T | T | T | F |
b [5] | F | F | F | T |


Step 1: Create a dp 2D array with blank item for "s" and "regex" with "s" horizontally and "regex" vertically.
Step 2: We set dp[0][0] as True.
Step 3: Fill all the other elements in first row with False because an empty regex pattern will not match any string
Step 4: The first column needs to filled based on the following conditions
        - True if dp[i][0] == '*' and dp[i-2][0] == True
            Because dp[i-2][0] is True then as per regex pattern .* can be 0 or more occurences so if it is True till dp[i-2][0] then it will be True after adding .*

        - False for any other case.

Step 5: In this step we will fill up the whole 2-D array starting with row = 1 and column = 1 and the values will be filled up based on few conditions

        - if regex[i] == s[j] or regex[i] == '.'
            then we must check whether the current regex subset - 1 character matches with the current substring - 1 character
            i.e. if dp[i-1][j-1] is True then dp[i][j] also becomes True

        - if regex[i] = '*' then 
            we must check two conditions
                1. whether the matching was true even without the current addition of .*
                    OR
                2. whether the current char with * is same as the current character in the string and 
                    with removing the current character also it matches with the current regex including .*
                
            For example if we see dp[4][4] from the above set of example then
            in dp[4][4] we are trying to match string "aa" with regex "c*a*"

            therefore we can only say dp[4][4] is True only if 

            1. without including the last "a*" in regex the string matches, so dp[2][4] must be True
                OR
            2. current char from the string that is "a" must match with the character having "*" in the regex 
                AND 
               even without including the current character in the string it must match the regex.

            
            Because "c*a*" can match the following "c*" or "c*aa*" so we are checking for these 2 conditions

            "c*aa*" matches only if "c*a" matches with current substring without the last character
                AND
            the last / current character from the substring we are matching for must match with the character for which '*' is present in the current position.

Step 6: Once the dp 2-D array is populated the item in dp[rLen][sLen], i.e. the last item gives us the answer whether the string matches the regex or not.

'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:        
        s = ' ' + s
        p = ' ' + p
        
        sLen = len(s)
        pLen = len(p)

        dp = [[False for x in range(sLen)] for y in range(pLen)]
        
        dp[0][0] = True
        
        for i in range(1, pLen):
            if p[i] == '*' and i > 1:
                dp[i][0] = dp[i-2][0]
            else:
                dp[i][0] = False
        

        for i in range(1, pLen):
            for j in range(1, sLen):
                if p[i] == '*':
                    dp[i][j] = ((p[i-1] == s[j] or p[i-1] == '.') and dp[i][j-1]) or (i >= 2 and dp[i-2][j])
                        
                elif (p[i] == '.' or p[i] == s[j]):
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = False

        return dp[pLen-1][sLen-1]
 