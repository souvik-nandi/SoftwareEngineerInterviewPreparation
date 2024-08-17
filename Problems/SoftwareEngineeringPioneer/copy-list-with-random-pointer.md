# 138. Copy List with Random Pointer

## Problem Description
You are given a linked list with `next` and `random` pointers. Each node in the linked list has a `val` (value), a `next` pointer to the next node in the list, and a `random` pointer that may point to any node in the list or be `None`.

Your task is to create a deep copy of the linked list. The copied list should have the same structure and values as the original list, including the `random` pointers.

### Example
- **Input:** `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`
- **Output:** `[[7,null],[13,0],[11,4],[10,2],[1,0]]`

### Node Definition

```python
class Node:
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
```

## Solution 1: Using Hash Map

### Algorithm

1. **Create Node Copies**
   - Traverse the original list and create a copy of each node.
   - Store the mapping between the original nodes and their copied nodes in a dictionary.

2. **Assign Pointers**
   - Traverse the original list again.
   - For each node, use the mapping to set the `next` and `random` pointers of the copied nodes.

3. **Return the Copied List**
   - Return the head of the new copied list, which can be accessed from the mapping.

### Code

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Step 1: Create a mapping from original nodes to their copies
        oldToNew = {None: None}

        curNode = head
        while curNode:
            # Create a copy of the current node and add it to the mapping
            oldToNew[curNode] = Node(curNode.val)
            curNode = curNode.next

        # Step 2: Assign the next and random pointers to the copied nodes
        curNode = head
        while curNode:
            # Set the next pointer of the copied node
            oldToNew[curNode].next = oldToNew[curNode.next]
            # Set the random pointer of the copied node
            oldToNew[curNode].random = oldToNew[curNode.random]
            curNode = curNode.next

        # Step 3: Return the head of the copied list
        return oldToNew[head]
```

### Complexity
- **Time Complexity:** `O(n)`, where `n` is the number of nodes in the list. Each node is processed twice (once for copying and once for assigning pointers).
- **Space Complexity:** `O(n)`, due to the space required for the dictionary storing the mapping of nodes.

## Solution 2: Interleaving Nodes

### Algorithm

1. **Interleave Nodes**
   - Insert each copied node directly after its original node in the list.

2. **Assign Pointers**
   - Update the `random` pointers of the copied nodes.

3. **Separate Lists**
   - Restore the original list and extract the copied list.

### Code

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # First Pass: Create a new node for each original node and link them together.
        curNode = head
        while curNode:
            newNode = Node(curNode.val, curNode.next)
            curNode.next = newNode
            curNode = newNode.next
        
        # Second Pass: Assign random pointers to the new nodes.
        curNode = head
        while curNode:
            if curNode.random:
                curNode.next.random = curNode.random.next
            curNode = curNode.next.next
        
        # Third Pass: Separate the two lists.
        curNode = head
        newHead = head.next
        while curNode:
            newNode = curNode.next
            curNode.next = newNode.next
            newNode.next = newNode.next.next if newNode.next else None
            curNode = curNode.next
        
        return newHead
```

### Complexity
- **Time Complexity:** `O(n)`, where `n` is the number of nodes in the list. Each node is processed three times.
- **Space Complexity:** `O(1)`, since no additional data structures are used.

## Comparison

### Hash Map Approach
- **Pros:**
  - **Simplicity:** Easy to understand and implement.
  - **Direct Mapping:** Provides a clear and direct way to map nodes and set pointers.
- **Cons:**
  - **Space Complexity:** Requires additional space for the hash map, which may be a concern for very large lists.

### Interleaving Nodes Approach
- **Pros:**
  - **Space Efficiency:** Does not require extra space for mapping nodes, as nodes are interleaved and separated in place.
- **Cons:**
  - **Complexity:** Slightly more complex to implement due to multiple passes and the need to manage pointers directly.

### Conclusion
- **Hash Map Approach:** Preferred for its simplicity and directness. Easier to implement and understand, making it suitable for scenarios where space is not a major constraint.
- **Interleaving Nodes Approach:** Chosen for its space efficiency, particularly when dealing with large lists where memory usage is a concern. However, it is more complex to implement.

The choice between the two approaches depends on specific requirements such as space constraints and implementation preferences. Both approaches efficiently solve the problem but offer different trade-offs.
