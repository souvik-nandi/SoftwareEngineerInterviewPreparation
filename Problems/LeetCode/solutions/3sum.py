'''

Problem Statement: 3Sum

Link: https://leetcode.com/problems/3sum
Tags: ['Array', 'Two Pointers']
Difficulty: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
 
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = []
Output: []
Example 3:
Input: nums = [0]
Output: []

 
Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

'''

'''
Solution:

Algorithm:
    1) Sort the list (will be required for 2 pointer search and removing duplicated)
    2) Iterate over each item to fix 'i'
    3) Run a 2 pointer loop one starting from i + 1 and another from n - 1 until j < k
        j -> i+1
        k -> n-1

    4) if sum(vals(i, j, k)) == 0, then increment j
    5) elif sum(vals(i, j, k)) < 0, then increment j
    6) else sum(vals(i, j, k)) > 0, then decrement k
    

Till this much it will provide all possible triplets with sum = 0, but there will be  duplicates 

Inorder to remove the duplicates same value should not appear for i and j
So we will add two more checks
    2.1) if val(i) == val(i-1) continue
    4.1) if j < k and val(j) == val(j-1) keep incrementing j
'''


'''
    Most fastest solution for 3 sum
'''
from typing import List
from bisect import bisect_left
import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        counter = collections.defaultdict(int)
        for i in nums:
            counter[i] += 1
        nums = sorted(counter)
        
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        output = []

        for i in range(len(nums) - 2):
            i_item = nums[i]
            twoSum = -i_item
            min_half, max_half = twoSum - nums[-1], twoSum / 2
            l = bisect_left(nums, min_half, i+1)
            r = bisect_left(nums, max_half, l)

            for j_item in nums[l:r]:                
                k_item = twoSum - j_item
                
                if k_item in counter:
                    output.append([i_item, j_item, k_item])

        for k in counter:
            if counter[k] > 1:
                if k == 0 and counter[k] >= 3:
                    output.append([0,0,0])
                elif k != 0 and -2*k in counter:
                    output.append([k, k, -2*k])
        return output
            
'''
    Most generalized solution using kSum
'''

class Solution:
    def twoSum(self, nums, target):
        l, r = 0, len(nums) - 1
        combs = []
        while l < r:
            tot = nums[l] + nums[r]

            if tot < target or (l > 0 and nums[l] == nums[l-1]):
                l += 1
            elif tot > target or (r < len(nums) - 1 and nums[r] == nums[r+1]):
                r -= 1
            else:
                combs.append([nums[l], nums[r]])
                l += 1
                r -= 1

        return combs
    
    def kSum(self, nums, target, k):
        if len(nums) < k or sum(nums[0:k]) > target or sum(nums[-k:]) < target:
            return []
        if k == 2:
            return self.twoSum(nums, target)
        combs = []
        
        for i in range(len(nums) - k + 1):
            if i == 0 or nums[i] != nums[i-1]:
                for item in self.kSum(nums[i+1:], target - nums[i], k - 1):
                    combs.append([nums[i]] + item)
        
        return combs
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.kSum(sorted(nums), 0, 3)
