'''

Problem Statement: 3Sum Closest

Link: https://leetcode.com/problems/3sum-closest
Tags: ['Array', 'Two Pointers']
Difficulty: Medium

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
 
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

 
Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4



'''

'''
Solution:

This solution expects non-repeating indexes.
Check 3sum.py for the algorithm
'''


from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n < 3:
            return []
        
        triplet_sum = nums[0] + nums[1] + nums[2]
        nums = sorted(nums)
        
        for i in range(n):
            # Never let i refer to the same value twice to avoid duplicates.
            if (i != 0 and nums[i] == nums[i - 1]): continue;
            j = i + 1
            k = n - 1
            
            # Two pointer search starts
            while j < k:                
                tot = nums[i] + nums[j] + nums[k]
                
                if abs(tot - target) < abs(triplet_sum - target):
                    triplet_sum = tot

                if tot == target:
                    break
                if tot < target:
                    j += 1
                    # Never let j refer to the same value twice (in an output) to avoid duplicates.
                    while (j < k and nums[j] == nums[j-1]): j += 1;
                else:
                    k -= 1
                    
            if tot == target:
                break
        
        return triplet_sum
