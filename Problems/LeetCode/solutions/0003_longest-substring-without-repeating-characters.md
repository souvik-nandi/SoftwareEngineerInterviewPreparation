# 3. Longest Substring Without Repeating Characters

## Problem

<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without repeating characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
    <li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>

## Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the most recent index of each character
        charIndex = {}
        # Variable to track the maximum length of substring without repeating characters
        maxLen = 0
        # Variable to track the start index of the current substring
        start = 0

        # Iterate through the string
        for i, c in enumerate(s):
            # If the current character is already seen in the substring and its index is after the start index
            if c in charIndex and charIndex[c] >= start:
                # Update the start index to the index after the last occurrence of the character
                start = charIndex[c] + 1

            # Update the index of the current character
            charIndex[c] = i
            # Calculate the length of the current substring and update maxLen if needed
            maxLen = max(maxLen, i - start + 1)

        # Return the maximum length of substring without repeating characters
        return maxLen
```

Explanation:

- Dictionary to Store Character Indices: We use a dictionary (charIndex) to store the most recent index of each character encountered in the string s. This dictionary helps us quickly determine if a character has been seen before and its last occurrence's position.

- Variables Initialization: We initialize maxLen to 0 to keep track of the maximum length of the substring without repeating characters. We also initialize start to 0, which represents the start index of the current substring.

- Iterating Through the String: We iterate through the string s using the enumerate function to get both the character c and its index i.

- Updating Start Index: If the current character c is found in the charIndex dictionary, and its last occurrence's index (charIndex[c]) is greater than or equal to the start index, it means that c is repeating in the current substring. In this case, we update the start index to one position after the last occurrence of c, ensuring that the substring contains no repeating characters.

- Updating Character Index: We update the index of the current character c in the charIndex dictionary to the current index i. This step ensures that we always have the most recent index of each character.

- Calculating Maximum Length: At each iteration, we calculate the length of the current substring (i - start + 1) and update maxLen if the length exceeds the previous maximum length.

- Returning Maximum Length: After iterating through the entire string, we return the final value of maxLen, which represents the length of the longest substring without repeating characters.

Overall, this solution maintains a sliding window approach, where the start index marks the beginning of the current substring, and we expand the window by moving the start index forward whenever we encounter repeating characters. The time complexity of this solution is O(n), where n is the length of the input string s, as it only requires a single pass through the string.
