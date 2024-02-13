# 1. Two Sum

## Problem

<p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
    <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
    <li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
    <li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?

## Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the index of each number in the list
        numsIndexMap = {}

        # Iterate through the list of numbers
        for idx, num in enumerate(nums):
            # Calculate the remaining value needed to reach the target
            remainingVal = target - num

            # Check if the remaining value is already in the dictionary
            if remainingVal in numsIndexMap:
                # If found, return the indices of the two numbers
                return [numsIndexMap[remainingVal], idx]
            else:
                # If not found, store the current number's index in the dictionary
                numsIndexMap[num] = idx

        # If no solution is found, return [-1, -1]
        return [-1, -1]
```

Explanation:

- We use a dictionary numsIndexMap to store the indices of the numbers encountered so far.
- For each number in the list, we calculate the remaining value needed to reach the target.
- We check if the remaining value is already in the dictionary. If it is, it means we have found a pair that sums up to the target.
- If the remaining value is not found in the dictionary, we store the current number's index in the dictionary.
- If no solution is found after iterating through the entire list, we return [-1, -1] indicating no solution.
