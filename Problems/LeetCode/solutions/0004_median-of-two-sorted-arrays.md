# 4. Median of Two Sorted Arrays

## Problem

<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>nums1.length == m</code></li>
    <li><code>nums2.length == n</code></li>
    <li><code>0 &lt;= m &lt;= 1000</code></li>
    <li><code>0 &lt;= n &lt;= 1000</code></li>
    <li><code>1 &lt;= m + n &lt;= 2000</code></li>
    <li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>

## Solution

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for simplicity
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n1, n2 = len(nums1), len(nums2)
        total_len = n1 + n2
        left_partition_size = (n1 + n2 + 1) // 2

        # Initialize search range for binary search
        low, high = 0, n1

        while low <= high:
            # Binary search to find the partition in nums1
            partition_nums1 = (low + high) // 2
            partition_nums2 = left_partition_size - partition_nums1

            # Determine values at the partition
            l1 = nums1[partition_nums1 - 1] if partition_nums1 > 0 else float('-inf')
            l2 = nums2[partition_nums2 - 1] if partition_nums2 > 0 else float('-inf')
            r1 = nums1[partition_nums1] if partition_nums1 < n1 else float('inf')
            r2 = nums2[partition_nums2] if partition_nums2 < n2 else float('inf')

            # Check if partitions are valid
            if l1 <= r2 and l2 <= r1:
                # Determine median based on even or odd total length
                if total_len % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                # Adjust search range to the left in nums1
                high = partition_nums1 - 1
            else:
                # Adjust search range to the right in nums1
                low = partition_nums1 + 1

        return 0  # Default return if input arrays are empty
```

Explanation:

- Ensure nums1 is the smaller array for simplicity. If not, swap nums1 and nums2.
- Initialize variables to store the lengths of nums1 and nums2, and calculate the total length of the combined array.
- Calculate the size of the left partition, which is half of the total length rounded up. This represents the number of elements that should be on the left side of the combined array to find the median.
- Initialize a binary search to find the correct partition in nums1.
- Inside the binary search loop:
- Calculate the partition indices for both arrays.
- Determine the elements to the left and right of the partitions for both arrays.
- Check if the partitions are valid. If so, calculate the median based on the values at the partitions.
- If not, adjust the search range based on the comparison of elements at the partition points.
- Return the calculated median value or 0 if the input arrays are empty.
