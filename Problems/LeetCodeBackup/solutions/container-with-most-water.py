'''

Problem Statement: Container With Most Water

Link: https://leetcode.com/problems/container-with-most-water
Tags: ['Array', 'Two Pointers']
Difficulty: Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.
 
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2

 
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104



'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        linesCount = len(heights)
        maxHeight = max(heights)
        
        start = 0
        end = linesCount - 1
        
        maxArea = 0
        
        while start < end and (end - start) * maxHeight >= maxArea:   
            area = min(heights[end], heights[start]) * (end - start)
            
            if area > maxArea:
                maxArea = area
            
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
            
                
        return maxArea



'''
Explaination:


Approach is to solve this in O(n) runtime.

We will take 2 pointers one pointing to start of the list and another pointing to the end.
And the approach is the increase any one pointer and calculate the area and comparing with maxArea variable.

So far it sounds good but how do we increase the pointer, which pointer shall we increase the start or the end.

Lets us evaluate this

[h1, h2, h3, h4, h5, h6]

start -> h1
end -> h6

we got area = (endPos - startPos) * min(h1, h6)

now our target is to maximize the area, so our next step should be to find the next possible combination where area can be maximized

if h1 < h6, then there is a chance that the combination of (h2, h6) will give maximized area
else there is chance that (h1, h5) will give the maximize the area.

Our approach should be increase the value of min(heights[start], height[end])
and inorder to do so we will be holding position of the height which is more and changing the one which points to the lower one

Say if h1 < h6, then we will hold position of end that points to h6 and increase the start pointer in order find a better combination.
Else if h1 > h6, then we will hold position of start that points to h1 and decrease the end pointer in order find a better combination.


But how long shall this process go on, the process should terminate in either or the 2 cases.

1) start >= end, 
    the difference becomes 0 or negative

2) (end - start) * maxHeightInTheList < maxAreaTillNow, 
    in this case if we futher change the pointers it will just decrease the value of (end - start) 
    and since (end - start) * maxHeightInTheList is already less than the maxAreaTillNow 
    then in the next iterations it can never give any value greater than maxAreaTillNow.

'''