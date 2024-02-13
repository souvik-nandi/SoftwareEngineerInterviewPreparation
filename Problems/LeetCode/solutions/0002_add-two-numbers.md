# 2. Add Two Numbers

## Problem

<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
    <li><code>0 &lt;= Node.val &lt;= 9</code></li>
    <li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a new linked list with a dummy node
        newList = ListNode(0)
        # Pointer to iterate through the new linked list
        ptr = newList
        # Initialize carry to 0
        carry = 0

        # Loop until both input linked lists are exhausted and there is no carry
        while l1 or l2 or carry:
            # Initialize the values of l1 and l2 to 0
            l1val = 0
            l2val = 0

            # If l1 is not None, update l1val and move to the next node
            if l1:
                l1val = l1.val
                l1 = l1.next
            # If l2 is not None, update l2val and move to the next node
            if l2:
                l2val = l2.val
                l2 = l2.next

            # Calculate the sum of current digits and the carry from the previous iteration
            final = l1val + l2val + carry
            # If the sum is less than 10, set carry to 0, otherwise set carry to 1 and take the modulo
            final, carry = (final, 0) if final < 10 else (final % 10, 1)

            # Create a new node with the final value
            newNode = ListNode(final)
            # Connect the new node to the previous node in the new linked list
            ptr.next = newNode
            # Move the pointer to the new node
            ptr = newNode

        # Return the next node of the dummy node, which is the head of the new linked list
        return newList.next
```

Explanation:

- We initialize a new linked list with a dummy node to simplify the logic.
- We use a pointer ptr to iterate through the new linked list.
- We initialize carry to 0 to keep track of any carry from the addition of digits.
- We loop until both input linked lists are exhausted and there is no carry left.
- In each iteration, we extract the values of the current digits from l1 and l2, and calculate the sum along with the carry.
- We create a new node with the final value, connect it to the previous node in the new linked list, and update the pointer ptr to the new node.
- Finally, we return the next node of the dummy node, which is the head of the new linked list.
