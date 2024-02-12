'''

Problem Statement: Next Permutation

Link: https://leetcode.com/problems/next-permutation
Tags: ['Array']
Difficulty: Medium

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.
 
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:
Input: nums = [1]
Output: [1]

 
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100



'''

from typing import List


class Solution:
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i > -1:
            # find the next max
            j = n - 1
            while j > i and nums[i] >= nums[j]:
                j -= 1

            # swap the values in i and j
            nums[i], nums[j] = nums[j], nums[i]

        # reverse the remaining range, when i = -1 is the whole list gets reversed
        self.reverse(nums, i + 1, n - 1)
