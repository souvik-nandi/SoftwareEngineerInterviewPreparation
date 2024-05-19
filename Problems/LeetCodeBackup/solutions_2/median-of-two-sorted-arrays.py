'''

Problem Statement: Median of Two Sorted Arrays

Link: https://leetcode.com/problems/median-of-two-sorted-arrays
Tags: ['Array', 'Binary Search', 'Divide and Conquer']
Difficulty: Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
 
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

 
Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106



'''



'''
Solution:

nums1 and nums2 are the two list and are already sorted.
The brute force approach of finding the median can be to merge both the lists and sort it and then find the median. [Time complexity: O((m + n)Log(m + n)]
Another approach can be to merge the sorted lists using pointer approach and then find the median. [Time complexity: O(m + n)]

Here is an approach which can be used to reduce the time complexity extensively. [Time complexity: O(log(min(m, n)))]

Q: What is the approach ?
A: Since the lists are already sorted and our objective is to find the median (the middle element / value of a sorted list), 
    we basically need to find an element which will divide the sorted elements after merging the lists into two equal parts.



The following solution tries to solve the problem in different levels, starting from basic then adapting to multiple conditions that can arise.

Level 1: 
    The total length of list elements combined is odd, so we can get the exact element and no requirement to average two elements.
    Even though we need to search the element and since the elements are already sorted we will use binary search but will consider that in
    the first iteration of search the element will be found.


Level 2:
    The element is not found in the first iteration of binary search

Level 2: 
    If binary search is unable to find the element, can happen since we will try to run 
    binary search on the list with less elements to reduce time complexity.

Level 3:
    Even number of elements after combining the lists, so it will require find two elements and then providing the average of those as median.






################################################################### LEVEL 1 ######################################################################

Lets take an example and understand.

nums1 = [2, 4, 9]
nums2 = [1, 2, 3, 5, 6, 7]
m = len(nums1) = 3
n = len(nums2) = 6
total number of elements = 9
then for the median there must be 4 items which will be smaller or equal
and there must be 4 items which will be larger or equal

In this case if we see [1, 2, 2, 3,  || 4 ||   5, 6, 7, 9]


Since it is faster to search in the smaller list (nums1 in this case), we will start by finding the element in nums1

[2, 4, 9]

When binary search starts we get [ start = 0, end = m - 1 = 2, midIndexOfNums1 = (start + end) // 2 = 1]
median position index for merged lists (midPoint) = (sum of length of lists) // 2 = 9 // 2 = 4
then the midIndexOfNums2 = midPoint - midIndexOfNums1 - 1 = 4 - 1 - 1 = 2

Condition for confirming the median:
"If element at midIndexOfNums1 in nums1 is the median 
then all the elements from beginning till midIndexOfNums2 in nums2 must be smaller or equal to nums1[midIndexOfNums1] 
and all the elements after midIndexOfNums2 in nums2 must be greater or equal to nums1[midIndexOfNums1],
since elements are already sorted checking only 
((nums1[midIndexOfNums1] >= nums2[midIndexOfNums2]) and (nums1[midIndexOfNums1] <= nums2[midIndexOfNums2 + 1]))
satisfies our condition"

In the above example we can see that 4 becomes the median, but the above conditions worked only because the median element existed in nums1.
what if nums1 does not have the median element but we still want to run the binary search on nums1 since it has less elements than nums2, 
to handle this case we need to check the above conditions one more time just by reversing the nums1 and nums2

Lets take another example :

nums1 = [2, 3, 9]
nums2 = [1, 2, 4, 5, 6, 7]

When binary search starts we get [ start = 0, end = m - 1 = 2, midIndexOfNums1 = (start + end) // 2 = 1]
median position index for merged lists (midPoint) = (sum of length of lists) // 2 = 9 // 2 = 4
then the midIndexOfNums2 = midPoint - midIndexOfNums1 - 1 = 4 - 1 - 1 = 2

Updated conditions:
1) nums1[midIndexOfNums1] becomes the median if 
((nums1[midIndexOfNums1] >= nums2[midIndexOfNums2]) and (nums1[midIndexOfNums1] <= nums2[midIndexOfNums2 + 1])) satisfies

OR

2) nums2[midIndexOfNums2] becomes the median if 
((nums2[midIndexOfNums2] >= nums1[midIndexOfNums1]) and (nums2[midIndexOfNums2] <= nums1[midIndexOfNums1 + 1])) satisfies








################################################################### LEVEL 2 ######################################################################

So far we are good with above examples and conditions since we got the median element in the first iteration of binary search,
what if we do not get out median element in the first iteration and we need to update the "start" or "end" values of binary search,
upon which circumstances shall we update "start" or "end" ?


3) if both the above condition fails and (nums1[midIndexOfNums1] < nums2[midIndexOfNums2])
then we need to search for elements greater than nums1[midIndexOfNums1] so we should update
start = midIndexOfNums1 + 1

4) if all the above conditions fails then we need know nums1[midIndexOfNums1] is larger
then we need to search for elements lesser than nums1[midIndexOfNums1] so we should update
end = midIndexOfNums1


So far the conditions set is
[
    1) nums1[midIndexOfNums1] becomes the median if 
    ((nums1[midIndexOfNums1] >= nums2[midIndexOfNums2]) and (nums1[midIndexOfNums1] <= nums2[midIndexOfNums2 + 1])) satisfies

    2) nums2[midIndexOfNums2] becomes the median if 
    ((nums2[midIndexOfNums2] >= nums1[midIndexOfNums1]) and (nums2[midIndexOfNums2] <= nums1[midIndexOfNums1 + 1])) satisfies

    3) if both the above condition fails and (nums1[midIndexOfNums1] < nums2[midIndexOfNums2])
    then we need to search for elements greater than nums1[midIndexOfNums1] so we should update
    start = midIndexOfNums1 + 1

    4) if all the above conditions fails then we need know nums1[midIndexOfNums1] is larger
    then we need to search for elements lesser than nums1[midIndexOfNums1] so we should update
    end = midIndexOfNums1
]








################################################################### LEVEL 3 ######################################################################


The above conditions works well but what if we are unable to find any element which satisfies to become the median even after the binary search ends.
If such a condition arises then we are sure that the median element is not present in nums1 list and there will be no element from nums1 list which 
can lie in the range [nums2[0], nums2[medianElementPosition]].

So what we can do is concat nums1 and nums2 and then find the median based on index.
But how do we concat the lists, what will be the order, should we do (nums1 + nums2) or (nums2 + nums1).

1) If nums1[m - 1] < nums2[0] then
we should concat in the following order (nums1 + nums2)

2) Else for any other conditions we should concat in the following order (nums2 + nums1)
Here we are not limiting the condition to (nums2[n - 1] < nums1[0]) instead using an else condition 
because it is not necessarily true that (nums2[n - 1] < nums1[0]) but instead (nums2[medianElementPosition] < nums1[0]) is true.
Since we do not care about what is present after medianElementPosition in nums2 we can safely concat in the following order (nums2 + nums1)
and find the median element position.







################################################################### LEVEL 4 ######################################################################


Till now everything will work but will fail at one point when the total number of elements (m + n) is even.
For example: 
In this list [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5 

We have not handled this case till now.
This case can be easily handled when we do no find the median element using binary search and 
concat in either of the ways (nums1 + nums2) or (nums2 + nums1), we just need to check if the total size 
is even or not and act accordingly.

But how do we do it when we find a median element using binary search, here also we get 2 more choices.

1) If the median element is from nums1 list
    then median can be 
    ((nums1[midIndexOfNums1] + nums1[midIndexOfNums1 - 1]) / 2)
    or
    ((nums1[midIndexOfNums1] + nums2[midIndexOfNums2]) / 2)

    #Note: If midIndexOfNums1 == 0 then (midIndexOfNums1 - 1) is underflow, so in this case 
    ((nums1[midIndexOfNums1] + nums2[midIndexOfNums2]) / 2) will be the median.

    1.1) ((nums1[midIndexOfNums1] + nums1[midIndexOfNums1 - 1]) / 2) is median when
            midIndexOfNums1 > 0 
            and
            nums1[midIndexOfNums1 - 1] > nums2[midIndexOfNums2]  
            
            # To handle the underflow condition
            # nums1[midIndexOfNums1 - 1] and nums2[midIndexOfNums2] both are less than equal to nums1[midIndexOfNums1], 
            # so the greater one should be used in calculating the median
    
    1.2) If the above condition does not satisfy then the median is ((nums1[midIndexOfNums1] + nums2[midIndexOfNums2]) / 2)




2) If the median element is from nums2 list
    then median can be 
    ((nums2[midIndexOfNums2] + nums2[midIndexOfNums2 - 1]) / 2)
    or
    ((nums2[midIndexOfNums2] + nums1[midIndexOfNums1]) / 2)

    #Note: If midIndexOfNums2 == 0 then (midIndexOfNums2 - 1) is underflow, so in this case 
    ((nums2[midIndexOfNums2] + nums1[midIndexOfNums1]) / 2) will be the median.

    1.1) ((nums2[midIndexOfNums2] + nums2[midIndexOfNums2 - 1]) / 2) is median when
            midIndexOfNums2 > 0 
            and
            nums2[midIndexOfNums2 - 1] > nums1[midIndexOfNums1]  
            
            # To handle the underflow condition
            # nums2[midIndexOfNums2 - 1] and nums1[midIndexOfNums1] both are less than equal to nums2[midIndexOfNums2], 
            # so the greater one should be used in calculating the median
    
    1.2) If the above condition does not satisfy then the median is ((nums2[midIndexOfNums2] + nums1[midIndexOfNums1]) / 2)


'''

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 

        # Median function for a single sorted array     
        def findMedian(arr):
            lenOfArr = len(arr)
            if lenOfArr == 0:
                return 0
            if lenOfArr % 2 == 0:
                return (arr[lenOfArr // 2 - 1] + arr[lenOfArr // 2]) / 2
            return arr[lenOfArr // 2]
        
        
        # Storing the number of items present in nums1 and nums2
        m = len(nums1)
        n = len(nums2)
        
        # The idea is to store the smaller array in nums1
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        # Initializing the variables for binary search operation on the smaller array
        start = 0
        midPoint = (m + n) // 2
        end = min(m - 1, midPoint) # Handles the out of index condition
        
        # Variables that will be used to store the median index either from nums1 or nums2
        requiredIndexOfM = -1
        requiredIndexOfN = -1
        
        # If any one of the list is empty then we can simply find the median directly from the non empty list since it is already sorted
        if (m == 0 or n == 0):
            return findMedian(nums1 + nums2)
        
        
        # Binary search initiated to find the median element
        while start <= end:
            mid = (start + end) // 2 # index in nums1

            # index in nums2 
            # when the required median is found then the elements till midOfN position should ideally be present on the left side 
            # of mid element in nums1 list
            midOfN = midPoint - mid - 1 
            

            if (midOfN == n - 1 or nums1[mid] <= nums2[midOfN + 1]) and (nums1[mid] >= nums2[midOfN]):
                requiredIndexOfM = mid
                break
            elif (mid == m - 1 or nums2[midOfN] <= nums1[mid + 1]) and (nums2[midOfN] >= nums1[mid]):
                requiredIndexOfN = midOfN
                break
            elif ((nums1[mid] < nums2[midOfN - 1] or midOfN == 0) or 
                 (nums1[mid] < nums2[midOfN])):
                start = mid + 1
            else:
                end = mid - 1

        
        if requiredIndexOfM > -1:
            if ((m + n) % 2 == 0):
                if requiredIndexOfM > 0 and nums1[requiredIndexOfM - 1] > nums2[midPoint - requiredIndexOfM - 1]:
                    return (nums1[requiredIndexOfM] + nums1[requiredIndexOfM - 1]) / 2
                else:
                    return (nums1[requiredIndexOfM] + nums2[midPoint - requiredIndexOfM - 1]) / 2
            else:
                return nums1[requiredIndexOfM]
        elif requiredIndexOfN > -1:
            if ((m + n) % 2 == 0):
                if requiredIndexOfN > 0 and nums2[requiredIndexOfN - 1] > nums1[midPoint - requiredIndexOfN - 1]:
                    return (nums2[requiredIndexOfN] + nums2[requiredIndexOfN - 1]) / 2
                else:
                    return (nums2[requiredIndexOfN] + nums1[midPoint - requiredIndexOfN - 1]) / 2
            else:
                return nums2[requiredIndexOfN]            
        elif nums1[m - 1] <= nums2[0]:
            return findMedian(nums1 + nums2)
        else:
            return findMedian(nums2 + nums1)

                
            
            